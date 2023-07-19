from django.db import models


class Ethnic(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "ethnics"
        ordering = ["-id"]
