from django.db import models
from django.contrib.postgres.fields import ArrayField

from service.framework.model.timestamped_model import TimeStampedModel


class NewsType(TimeStampedModel):
    name = models.CharField(max_length=255, db_collation='und-x-icu')

    def __str__(self):
        return self.name

    class Meta:
        db_table = "news_types"
        app_label = "newsType"
        ordering = ["-id"]
