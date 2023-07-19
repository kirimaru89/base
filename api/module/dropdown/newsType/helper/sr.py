from rest_framework.serializers import ModelSerializer
from ..models import NewsType


class NewsTypeSr(ModelSerializer):
    class Meta:
        model = NewsType
        exclude = ()
        read_only_fields = ("id",)
