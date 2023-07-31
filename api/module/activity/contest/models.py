from django.db import models
from module.account.staff.models import Staff
from service.framework.model.timestamped_model import TimeStampedModel
from service.date_service import DateService
from module.activity.contest.consts import ContestStatus


class Contest(TimeStampedModel):
    uid = models.CharField(max_length=255, unique=True)
    organizational_unit = models.CharField(max_length=255, blank=True, default="")
    title = models.CharField(max_length=255, unique=True)
    cover_image = models.TextField(null=True, blank=True)
    number_of_question = models.IntegerField(default=1)
    description = models.CharField(max_length=255, blank=True, null=True)
    duration = models.IntegerField()
    min_score = models.IntegerField()
    start_at = models.DateTimeField()
    end_at = models.DateTimeField()
    contest_organizer = models.CharField(max_length=255, blank=True, null=True)

    created_by = models.ForeignKey(
        Staff, on_delete=models.CASCADE, related_name="contest_created_by"
    )
    updated_by = models.ForeignKey(
        Staff, on_delete=models.CASCADE, related_name="contest_updated_by"
    )

    @property
    def status(self):
        now = DateService.now()
        if now < self.start_at:
            return ContestStatus.NOT_STARTED

        return ContestStatus.FINISHED if now > self.end_at else ContestStatus.STARTED

    def __str__(self):
        return self.title

    class Meta:
        db_table = "contests"
        ordering = ["-id"]
