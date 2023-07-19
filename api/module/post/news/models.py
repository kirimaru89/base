from django.db import models
from service.framework.model.timestamped_model import TimeStampedModel


class News(TimeStampedModel):
    news_type = models.ForeignKey("news.newsType", on_delete=models.DO_NOTHING)
    news_category = models.ForeignKey("news.newsType", on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=255, unique=True)
    content = models.TextField()
    cover_image = models.TextField()
    created_by = models.IntegerField(default=1)
    updated_by = models.IntegerField(default=1)
    status = models.SmallIntegerField()
    
    def __str__(self):
        return self.title

    class Meta:
        db_table = "news"
        ordering = ["-id"]
