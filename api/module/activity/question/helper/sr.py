from rest_framework.serializers import ModelSerializer
from ..consts import QUESTION_TYPE_DICT
from ..models import Question


class QuestionSr(ModelSerializer):
    class Meta:
        model = Question
        exclude = ()
        read_only_fields = ("id",)

    def to_representation(self, obj):
        from module.activity.answer.helper.sr import AnswerSr

        rep = super().to_representation(obj)
        rep["answers"] = AnswerSr(obj.answers.all().order_by("order"), many=True).data
        rep["type_obj"] = {
            "value": obj.type,
            "label": QUESTION_TYPE_DICT.get(obj.type, ""),
        }
        return rep
