import os
from django.urls import path

from .views import DeviceTokenView


BASE_ENDPOINT = DeviceTokenView.as_view(
    {"post": "add"}
)

PK_ENDPOINT = DeviceTokenView.as_view(
    {"delete": "delete"}
)


app_name = os.getcwd().split(os.sep)[-1]
urlpatterns = [
    path("", BASE_ENDPOINT),
    path("<str:registration_token>", PK_ENDPOINT),
]
