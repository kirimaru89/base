from rest_framework.serializers import ModelSerializer
from ..models import Category


class CategorySr(ModelSerializer):
    class Meta:
        model = Category
        exclude = ()
        read_only_fields = ("id",)
