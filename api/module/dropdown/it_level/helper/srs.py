from rest_framework.serializers import ModelSerializer
from module.dropdown.it_level.models import ItLevel


class ItLevelSr(ModelSerializer):
    class Meta:
        model = ItLevel
        exclude = ()
