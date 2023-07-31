from rest_framework.serializers import ModelSerializer
from ..models import Answer


class AnswerSr(ModelSerializer):
    class Meta:
        model = Answer
        exclude = ()
        read_only_fields = ("id",)
