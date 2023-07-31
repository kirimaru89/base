from django.db import models
from module.activity.contest.models import Contest
from .consts import QUESTION_TYPE_CHOICES, QuestionType


class Question(models.Model):
    contest = models.ForeignKey(
        Contest, on_delete=models.CASCADE, related_name="questions"
    )
    type = models.IntegerField(
        choices=QUESTION_TYPE_CHOICES,
        default=QuestionType.SINGLE,
        null=False,
        blank=False,
    )
    content = models.TextField()

    def __str__(self):
        return self.content

    class Meta:
        db_table = "questions"
        ordering = ["-id"]
