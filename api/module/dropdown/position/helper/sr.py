from rest_framework.serializers import ModelSerializer
from ..models import Position


class PositionSr(ModelSerializer):
    class Meta:
        model = Position
        exclude = ()
        read_only_fields = ("id",)


class PositionOptionSr(ModelSerializer):
    class Meta:
        model = Position
        exclude = ()

    def to_representation(self, obj):
        return {"value": obj.id, "label": obj.title}
