from rest_framework.serializers import ModelSerializer
from module.dropdown.position.models import Position


class PositionSr(ModelSerializer):
    class Meta:
        model = Position
        exclude = ()
