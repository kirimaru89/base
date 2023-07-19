from rest_framework.serializers import ModelSerializer
from module.dropdown.ethnic.models import Ethnic


class EthnicSr(ModelSerializer):
    class Meta:
        model = Ethnic
        exclude = ()
