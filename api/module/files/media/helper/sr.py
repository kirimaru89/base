from rest_framework.serializers import ModelSerializer
from ..models import Media


class MediaSr(ModelSerializer):
    class Meta:
        model = Media
        exclude = ()
        read_only_fields = ("id",)
