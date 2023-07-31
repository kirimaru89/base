from rest_framework.serializers import ModelSerializer
from ..consts import CONTEST_STATUS_DICT
from ..models import Contest


class ContestSr(ModelSerializer):
    class Meta:
        model = Contest
        exclude = ()
        read_only_fields = ("id",)

    def to_representation(self, obj):
        member = self.context.get("member")
        rep = super().to_representation(obj)
        rep["status"] = obj.status
        rep["status_obj"] = {
            "value": obj.status,
            "label": CONTEST_STATUS_DICT.get(obj.status, ""),
        }
        rep["created_by_obj"] = {
            "value": obj.created_by.pk,
            "label": obj.created_by.full_name,
        }
        rep["updated_by_obj"] = {
            "value": obj.updated_by.pk,
            "label": obj.updated_by.full_name,
        }
        rep["submitted_at"] = None
        rep["exam_id"] = None
        if member:
            if exam := (
                obj.exams.filter(member=member).order_by("-created_at").first()
            ):
                rep["submitted_at"] = exam.submitted_at
                rep["exam_id"] = exam.pk
        rep["number_of_questions"] = obj.questions.count()
        rep["participants"] = obj.exams.exclude(submitted_at=None).count()
        return rep
