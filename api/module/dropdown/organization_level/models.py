from django.db import models


class OrganizationLevel(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "organization_levels"
        ordering = ["-id"]
