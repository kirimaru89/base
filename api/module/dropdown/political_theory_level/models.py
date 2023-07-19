from django.db import models


class PoliticalTheoryLevel(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "political_theory_levels"
        ordering = ["-id"]
