from rest_framework.serializers import ModelSerializer
from ..models import Message


class MessageSr(ModelSerializer):
    class Meta:
        model = Message
        exclude = ()
        read_only_fields = ("id",)
