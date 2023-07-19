from django.db import models


class ItLevel(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "it_levels"
        ordering = ["-id"]
