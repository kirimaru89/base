from rest_framework.serializers import ModelSerializer
from module.dropdown.qualification.models import Qualification


class QualificationSr(ModelSerializer):
    class Meta:
        model = Qualification
        exclude = ()
