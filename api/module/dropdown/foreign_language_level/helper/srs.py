from rest_framework.serializers import ModelSerializer
from module.dropdown.foreign_language_level.models import ForeignLanguageLevel


class ForeignLanguageLevelSr(ModelSerializer):
    class Meta:
        model = ForeignLanguageLevel
        exclude = ()
