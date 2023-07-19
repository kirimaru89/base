from django.db import models


class NewsCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "news_categories"
        app_label = "news"
        ordering = ["-id"]
