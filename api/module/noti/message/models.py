from django.db import models
from service.framework.model.timestamped_model import TimeStampedModel
from module.account.member.models import Member
from .consts import SOURCE_TYPE_CHOICES, SourceType


class Message(TimeStampedModel):
    member = models.ForeignKey(
        Member,
        related_name="messages",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None,
    )
    title = models.CharField(max_length=255)
    source_type = models.IntegerField(
        choices=SOURCE_TYPE_CHOICES, default=SourceType.NEWS, null=False, blank=False
    )
    source_id = models.IntegerField()
    content = models.TextField()
    read_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "messages"
        ordering = ["-id"]
