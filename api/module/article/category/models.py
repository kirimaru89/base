from django.db import models
from django.contrib.postgres.fields import ArrayField
from service.framework.model.timestamped_model import TimeStampedModel


class Category(TimeStampedModel):
    title = models.CharField(max_length=255)
    parent = models.ForeignKey(
        "self",
        related_name="children",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    parent_ids = ArrayField(models.IntegerField(), default=list, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "categories"
        ordering = ["-id"]
