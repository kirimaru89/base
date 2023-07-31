from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    email = models.EmailField(
        max_length=128, unique=True, null=True, blank=True, default=None
    )
    mobile = models.CharField(
        max_length=64, unique=True, null=True, blank=True, default=None
    )
    refresh_token_signature = models.CharField(max_length=128, blank=True, default="")
    full_name = models.CharField(max_length=255, blank=True, default="")

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        self.username = self.email
        super().save(*args, **kwargs)

    class Meta:
        db_table = "users"
        ordering = ["-id"]
        verbose_name = _("user")
