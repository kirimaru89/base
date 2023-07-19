from rest_framework.serializers import ModelSerializer
from ..models import NewsCategory


class NewsCategorySr(ModelSerializer):
    class Meta:
        model = NewsCategory
        exclude = ()
        read_only_fields = ("id",)
