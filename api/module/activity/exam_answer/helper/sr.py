from rest_framework.serializers import ModelSerializer
from ..models import ExamAnswer


class ExamAnswerSr(ModelSerializer):
    class Meta:
        model = ExamAnswer
        exclude = ()
        read_only_fields = ("id",)
