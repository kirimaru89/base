from django.db import transaction
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated

from module.noti.device.helper.util import DeviceTokenUtils
from module.noti.device.models import DeviceToken
from service.request_service import RequestService


class DeviceTokenView(GenericViewSet):
    permission_classes = (IsAuthenticated,)

    @transaction.atomic
    @action(methods=["post"], detail=True)
    def add(self, request, *args, **kwargs):
        member = self.request.user.member
        data = request.data
        registration_token = data.get("registration_token", None)
        DeviceTokenUtils.empty_device_token(member, registration_token)

        data.update({"member": member.pk})
        exist_token = DeviceTokenUtils.get_exist_token(registration_token)
        if exist_token and exist_token.registration_token:
            data.update({"registration_token": registration_token})

        DeviceTokenUtils.register_device_token(data)
        return RequestService.res({})

    @action(methods=["delete"], detail=True)
    def delete(self, request, registration_token=None):
        member = self.request.user.member
        DeviceToken.objects.filter(
            member=member, registration_token=registration_token
        ).delete()
        return RequestService.res(status=status.HTTP_204_NO_CONTENT)
