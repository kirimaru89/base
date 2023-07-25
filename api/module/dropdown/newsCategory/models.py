from django.db import models
from django.contrib.postgres.fields import ArrayField
from service.framework.model.timestamped_model import TimeStampedModel


class NewsCategory(TimeStampedModel):
    name = models.CharField(max_length=255, db_collation='und-x-icu')
    parent = models.ForeignKey(
        "self",
        related_name="children",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    
    parent_ids = ArrayField(models.IntegerField(), default=list, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "news_categories"
        app_label = "newsCategory"
        ordering = ["-id"]
