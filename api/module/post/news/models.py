from django.db import models
from service.framework.model.timestamped_model import TimeStampedModel


class News(TimeStampedModel):
    news_type = models.ForeignKey("newsType.newsType", on_delete=models.DO_NOTHING)
    news_category = models.ForeignKey("newsCategory.newsCategory", on_delete=models.DO_NOTHING)
    created_by = models.ForeignKey("staff.staff", on_delete=models.DO_NOTHING, default=1, related_name="created_by")
    updated_by = models.ForeignKey("staff.staff", on_delete=models.DO_NOTHING, default=1, related_name="updated_by")
    
    title = models.CharField(max_length=255, unique=True)
    content = models.TextField()
    cover_image = models.TextField()
    status = models.SmallIntegerField()
    
    def __str__(self):
        return self.title

    class Meta:
        db_table = "news"
        ordering = ["-id"]
