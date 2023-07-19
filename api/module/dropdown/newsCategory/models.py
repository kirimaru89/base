from django.db import models
from service.framework.model.timestamped_model import TimeStampedModel


class NewsCategory(TimeStampedModel):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "news_categories"
        app_label = "newsCategory"
        ordering = ["-id"]
