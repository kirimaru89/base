from rest_framework.serializers import ModelSerializer
from module.activity.exam_question.helper.sr import ExamQuestionSr
from ..models import Exam


class ExamSr(ModelSerializer):
    class Meta:
        model = Exam
        exclude = ()
        read_only_fields = ("id",)

    def to_representation(self, obj):
        show_correct_answers = self.context.get("show_correct_answers", False)
        rep = super().to_representation(obj)
        rep["member_obj"] = {
            "value": obj.member.pk,
            "label": obj.member.full_name,
        }
        rep["contest_obj"] = (
            {
                "value": obj.contest.pk,
                "label": obj.contest.title,
            },
        )
        rep["questions"] = ExamQuestionSr(
            obj.exam_questions.all(),
            many=True,
            context=dict(show_correct_answers=show_correct_answers),
        ).data
        return rep
