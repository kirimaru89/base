from django.db import models
from module.activity.question.models import Question
from service.framework.model.timestamped_model import TimeStampedModel


class Answer(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="answers"
    )
    content = models.TextField()
    correct = models.BooleanField()
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.content

    class Meta:
        db_table = "answers"
        ordering = ["order"]
