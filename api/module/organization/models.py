from django.db import models
from django.contrib.postgres.fields import ArrayField
from phonenumber_field.modelfields import PhoneNumberField

from module.dropdown.organization_level.models import OrganizationLevel
from module.dropdown.organization_type.models import OrganizationType
from service.framework.model.timestamped_model import TimeStampedModel


class Organization(TimeStampedModel):
    parent = models.ForeignKey(
        "self",
        related_name="children",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    parent_ids = ArrayField(models.IntegerField(), default=list, blank=True)
    name = models.CharField(max_length=255)
    type = models.ForeignKey(
        OrganizationType, related_name="organizations", on_delete=models.SET_NULL, null=True, blank=True, default=None,
    )
    level = models.ForeignKey(
        OrganizationLevel, related_name="organizations", on_delete=models.SET_NULL, null=True, blank=True, default=None,
    )
    email = models.EmailField(
        max_length=128, unique=True, null=True, blank=True, default=None
    )
    phone_number = PhoneNumberField(unique=True, null=True, blank=True, default=None)
    representative = models.CharField(max_length=255, blank=True, default="")
    note = models.TextField(blank=True, default="")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "organizations"
        ordering = ["name"]

    @property
    def str(self):
        return ", ".join(
            list(
                Organization.objects.filter(
                    pk__in=[self.pk] + self.parent_ids
                )
                .order_by("level")
                .values_list("name", flat=True),
            ),
        )
