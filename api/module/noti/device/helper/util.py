from django.db.models import QuerySet

from module.noti.device.helper.sr import DeviceTokenSr
from module.noti.device.models import DeviceToken


class DeviceTokenUtils:
    @staticmethod
    def empty_device_token(
        member: QuerySet, registration_token: str = None
    ):
        DeviceToken.objects.filter(member=member).delete()
        return DeviceToken.objects.filter(
            registration_token=registration_token
        ).delete()

    @staticmethod
    def get_exist_token(registration_token):
        return DeviceToken.objects.filter(registration_token=registration_token).first()

    @staticmethod
    def register_device_token(data: dict):
        sr = DeviceTokenSr(data=data)
        sr.is_valid(raise_exception=True)
        sr.save()
