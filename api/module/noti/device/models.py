from django.db import models
from module.account.member.models import Member
from module.noti.device.consts import DEVICE_TYPES


class DeviceToken(models.Model):
    type = models.CharField(
        max_length=20, choices=DEVICE_TYPES, null=True, blank=True
    )
    registration_token = models.TextField(max_length=255)
    active = models.BooleanField(default=True)
    member = models.ForeignKey(
        Member,
        related_name="device_tokens",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return "{} device of member email {}: {}".format(
            self.type, self.member.user.username, self.registration_token
        )

    class Meta:
        db_table = "device_tokens"
        ordering = ["-id"]
