from rest_framework.serializers import ModelSerializer
from ..models import File


class FileSr(ModelSerializer):
    class Meta:
        model = File
        exclude = ()
        read_only_fields = ("id",)
