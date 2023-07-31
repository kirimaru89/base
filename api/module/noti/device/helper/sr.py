from rest_framework.serializers import ModelSerializer

from module.noti.device.models import DeviceToken


class DeviceTokenSr(ModelSerializer):
    class Meta:
        model = DeviceToken
        fields = "__all__"
        read_only_fields = ("id",)
