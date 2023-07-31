from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
from django.contrib.postgres.fields import ArrayField
from service.framework.model.timestamped_model import TimeStampedModel
from module.account.staff.models import Staff
from .consts import (
    CAMPAIGN_TYPE_CHOICES,
    CampaignType,
    BENEFICIARY_TYPE_CHOICES,
    BeneficiaryType,
)


class Campaign(TimeStampedModel):
    created_by = models.ForeignKey(
        Staff, on_delete=models.CASCADE, related_name="campaign_created_by"
    )
    updated_by = models.ForeignKey(
        Staff, on_delete=models.CASCADE, related_name="campaign_updated_by"
    )
    title = models.CharField(max_length=255, unique=True)
    cover_image = models.TextField()
    type = models.IntegerField(
        choices=CAMPAIGN_TYPE_CHOICES, default=CampaignType.HM, null=False, blank=False
    )
    content = models.TextField()
    place = models.CharField(max_length=255)
    registration_from = models.DateTimeField()
    registration_to = models.DateTimeField()
    occurring_time = models.CharField(max_length=255)
    beneficiary_types = ArrayField(models.IntegerField(), default=list)
    status = models.IntegerField()
    contact_email = models.EmailField(null=True, blank=True)
    contact_mobile = PhoneNumberField(unique=True, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "campaigns"
        ordering = ["-id"]
