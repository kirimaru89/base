from rest_framework.serializers import ModelSerializer
from module.dropdown.religion.models import Religion


class ReligionSr(ModelSerializer):
    class Meta:
        model = Religion
        exclude = ()
