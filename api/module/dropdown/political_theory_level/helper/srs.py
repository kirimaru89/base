from rest_framework.serializers import ModelSerializer
from module.dropdown.political_theory_level.models import PoliticalTheoryLevel


class PoliticalTheoryLevelSr(ModelSerializer):
    class Meta:
        model = PoliticalTheoryLevel
        exclude = ()
