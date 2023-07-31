from typing import List, Union
from django.db import models
from django.db.models import QuerySet
from service.framework.model.timestamped_model import TimeStampedModel
from django.contrib.postgres.fields import ArrayField
from .consts import (
    ORGANIZATION_TYPE_CHOICES,
    ORGANIZATION_LEVEL_CHOICES,
    OrganizationType,
    OrganizationLevel,
)


class OrganizationManager(models.Manager):
    def get_root_parent(self, obj: QuerySet) -> int:
        return self.get_root_parent(obj.parent) if obj and obj.parent else obj.pk

    def get_parents(
        self, item: QuerySet, field="pk", result=None
    ) -> List[Union[int, str]]:
        if result is None:
            result = []

        if not item or not item.parent:
            return result
        return self.get_parents(
            item.parent,
            field,
            result + [item.parent if field is None else getattr(item.parent, field)],
        )

    def get_childs(self, item: QuerySet, merge=False) -> list[int]:
        childs = self.filter(parent_ids__contains=[item.pk])
        return list(childs.values_list("id", flat=True))


class Organization(TimeStampedModel):
    parent = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="children"
    )
    root_parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="root_children",
    )
    parent_ids = ArrayField(models.IntegerField(), default=list, blank=True)
    title = models.CharField(max_length=255)
    type = models.IntegerField(
        choices=ORGANIZATION_TYPE_CHOICES,
        default=OrganizationType.DNNN,
        blank=False,
        null=False,
    )
    level = models.IntegerField(
        choices=ORGANIZATION_LEVEL_CHOICES,
        default=OrganizationLevel.CITY,
        blank=False,
        null=False,
    )
    rep_email = models.EmailField(max_length=255, null=True, blank=True, default=None)
    rep_mobile = models.CharField(max_length=64, null=False, blank=True, default="")
    rep_name = models.CharField(max_length=255, null=False, blank=True, default="")

    objects = OrganizationManager()

    def clean(self):
        self.parent_ids = Organization.objects.get_parents(self)
        root_parent_id = Organization.objects.get_root_parent(self)
        if self.pk == root_parent_id:
            self.root_parent = None
        else:
            self.root_parent_id = root_parent_id

    def save(self, *args, **kwargs):
        new_parent = self.parent
        old_parent = None
        if self.pk:
            if new_parent and new_parent.pk == self.pk:
                raise ValidationError({"parent": _("Tổ chức đoàn không hợp lệ")})
            old_obj = Organization.objects.get(pk=self.pk)
            old_parent = old_obj.parent

        self.clean()
        super().save(*args, **kwargs)

        if new_parent != old_parent:
            childs = Organization.objects.get_childs(self, True)
            childs = Organization.objects.filter(pk__in=childs)
            for child in childs:
                child.parents = Organization.objects.get_parents(child)
                child.save()

    def __str__(self):
        return self.title

    class Meta:
        db_table = "organizations"
        ordering = ["-id"]

    @property
    def str(self):
        return ", ".join(
            list(
                Organization.objects.filter(pk__in=[self.pk] + self.parent_ids)
                # .order_by("-level")
                .values_list("title", flat=True),
            ),
        )
