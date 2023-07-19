from django.db import models


class EducationLevel(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "education_levels"
        ordering = ["-id"]
