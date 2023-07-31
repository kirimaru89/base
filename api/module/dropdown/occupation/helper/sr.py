from rest_framework.serializers import ModelSerializer
from ..models import Occupation


class OccupationSr(ModelSerializer):
    class Meta:
        model = Occupation
        exclude = ()
        read_only_fields = ("id",)


class OccupationOptionSr(ModelSerializer):
    class Meta:
        model = Occupation
        exclude = ()

    def to_representation(self, obj):
        return {"value": obj.id, "label": obj.title}
