from django.db import models
from module.activity.exam.models import Exam
from service.framework.model.timestamped_model import TimeStampedModel


class ExamQuestion(models.Model):
    exam = models.ForeignKey(
        Exam, on_delete=models.CASCADE, related_name="exam_questions"
    )
    type = models.IntegerField()
    content = models.TextField()

    def __str__(self):
        return self.content

    class Meta:
        db_table = "exam_questions"
        ordering = ["-id"]
