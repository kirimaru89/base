from django.db import models
from module.activity.exam_question.models import ExamQuestion
from service.framework.model.timestamped_model import TimeStampedModel
from django.contrib.postgres.fields import ArrayField


class ExamResult(TimeStampedModel):
    exam_question = models.ForeignKey(
        ExamQuestion, on_delete=models.CASCADE, related_name="exam_results"
    )
    exam_answer_ids = ArrayField(models.IntegerField(), default=list)
    correct = models.BooleanField()

    def __str__(self):
        return self.exam_question.content

    class Meta:
        db_table = "exam_results"
        ordering = ["-id"]
