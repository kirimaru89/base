from rest_framework.serializers import ModelSerializer
from module.activity.exam_answer.models import ExamAnswer
from module.activity.exam_result.models import ExamResult
from ..models import ExamQuestion


class ExamQuestionSr(ModelSerializer):
    class Meta:
        model = ExamQuestion
        exclude = ()
        read_only_fields = ("id",)

    def to_representation(self, obj):
        from module.activity.exam_answer.helper.sr import ExamAnswerSr

        show_correct_answers = self.context.get("show_correct_answers", False)
        rep = super().to_representation(obj)
        rep["answers"] = ExamAnswerSr(obj.exam_answers.all(), many=True).data

        if show_correct_answers:
            rep["correct_answers"] = ExamAnswer.objects.filter(
                exam_question=obj, correct=True
            ).values_list("id", flat=True)
        else:
            rep["correct_answers"] = []

        submitted_answers = list(
            ExamResult.objects.filter(exam_question=obj).values_list(
                "exam_answer_ids", flat=True
            )
        )
        rep["submitted_answers"] = sum(submitted_answers, [])

        return rep
