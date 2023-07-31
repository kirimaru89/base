from rest_framework.serializers import ModelSerializer
from ..models import ExamResult


class ExamResultSr(ModelSerializer):
    class Meta:
        model = ExamResult
        exclude = ()
        read_only_fields = ("id",)
