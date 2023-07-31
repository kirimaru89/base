from django.db import models
from service.framework.model.timestamped_model import TimeStampedModel
from module.activity.campaign.models import Campaign
from .consts import CAMPAIGN_ATTACHMENT_TYPE_CHOICES, CampaignAttachmentType


class CampaignAttachment(TimeStampedModel):
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name='campaign_attachments')
    title = models.CharField(max_length=255)
    url = models.TextField()
    type = models.IntegerField(
        choices=CAMPAIGN_ATTACHMENT_TYPE_CHOICES,
        default=CampaignAttachmentType.IMAGE,
        null=False,
        blank=False,
    )

    def __str__(self):
        return self.title

    class Meta:
        db_table = "campaign_attachments"
        ordering = ["-id"]
