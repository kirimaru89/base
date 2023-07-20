from rest_framework.serializers import ModelSerializer

from module.activities_place.models import ActivitiesPlace


class ActivitiesPlaceSr(ModelSerializer):
    class Meta:
        model = ActivitiesPlace
        exclude = ()
