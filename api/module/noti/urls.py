import os
from django.urls import path, include

app_name = os.getcwd().split(os.sep)[-1]

urlpatterns = (
    path("verif/", include("module.noti.verif.urls", namespace="verif")),
    path("device/", include("module.noti.device.urls", namespace="device")),
    path("message/", include("module.noti.message.urls", namespace="message"))
)
