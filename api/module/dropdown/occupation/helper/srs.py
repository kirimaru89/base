from rest_framework.serializers import ModelSerializer
from module.dropdown.occupation.models import Occupation


class OccupationSr(ModelSerializer):
    class Meta:
        model = Occupation
        exclude = ()
