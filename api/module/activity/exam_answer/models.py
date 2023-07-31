from django.db import models
from module.activity.exam_question.models import ExamQuestion
from service.framework.model.timestamped_model import TimeStampedModel


class ExamAnswer(models.Model):
    exam_question = models.ForeignKey(
        ExamQuestion, on_delete=models.CASCADE, related_name="exam_answers"
    )
    content = models.TextField()
    correct = models.BooleanField()

    def __str__(self):
        return self.content

    class Meta:
        db_table = "exam_answers"
        ordering = ["-id"]
