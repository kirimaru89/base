from django.db import models


class Position(models.Model):
    title = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "positions"
        ordering = ["-id"]
