from rest_framework.serializers import ModelSerializer
from module.dropdown.education_level.models import EducationLevel


class EducationLevelSr(ModelSerializer):
    class Meta:
        model = EducationLevel
        exclude = ()
