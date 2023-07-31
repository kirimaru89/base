from django.db import models
from module.activity.contest.models import Contest
from module.account.member.models import Member
from service.framework.model.timestamped_model import TimeStampedModel


class Exam(TimeStampedModel):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="exams")
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE, related_name="exams")

    score = models.IntegerField(default=0)
    submitted_at = models.DateTimeField(default=None, null=True, blank=True)
    started_at = models.DateTimeField()
    finished_at = models.DateTimeField()

    def __str__(self):
        return " - ".join([self.member.user.full_name, self.contest.title])

    class Meta:
        db_table = "exams"
        ordering = ["-id"]
        permissions = (("submit_exam", "Nộp bài"),)
