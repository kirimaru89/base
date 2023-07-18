from django.db import models
from service.framework.model.timestamped_model import TimeStampedModel


class Recipient(TimeStampedModel):
    title = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "recipients"
        ordering = ["-id"]
