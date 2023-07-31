from django.db import models
from service.framework.model.timestamped_model import TimeStampedModel
from module.article.category.models import Category
from module.account.staff.models import Staff
from .consts import NEWS_TYPE_CHOICES, NewsType, NEWS_STATUS_CHOICES, NewsStatus


class News(TimeStampedModel):
    categories = models.ManyToManyField(Category)
    type = models.IntegerField(
        choices=NEWS_TYPE_CHOICES, default=NewsType.NORMAL, null=False, blank=False
    )
    status = models.IntegerField(
        choices=NEWS_STATUS_CHOICES, default=NewsStatus.ACTIVE, null=False, blank=False
    )
    title = models.CharField(max_length=255)
    content = models.TextField(default="")
    cover_image = models.TextField(default="")

    created_by = models.ForeignKey(
        Staff, on_delete=models.CASCADE, related_name="created_by"
    )
    updated_by = models.ForeignKey(
        Staff, on_delete=models.CASCADE, related_name="updated_by"
    )

    def __str__(self):
        return self.title

    class Meta:
        db_table = "news"
        ordering = ["-id"]
