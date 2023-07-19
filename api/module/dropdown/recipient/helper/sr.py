from rest_framework.serializers import ModelSerializer
from ..models import Recipient


class RecipientSr(ModelSerializer):
    class Meta:
        model = Recipient
        exclude = ()
        read_only_fields = ("id",)


class RecipientOptionSr(ModelSerializer):
    class Meta:
        model = Recipient
        exclude = ()

    def to_representation(self, obj):
        return dict(
            id=obj.id,
            name=obj.title,
        )
