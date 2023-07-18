from rest_framework.serializers import ModelSerializer
from ..models import Recipient


class RecipientSr(ModelSerializer):
    class Meta:
        model = Recipient
        exclude = ()
        read_only_fields = ("id",)
