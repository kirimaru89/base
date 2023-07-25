import os
from django.urls import path, include

from .views.crud import OrganizationViewSet

BASE_ENDPOINT = OrganizationViewSet.as_view(
    {"get": "list", "post": "add", "delete": "delete_list"}
)

PK_ENDPOINT = OrganizationViewSet.as_view(
    {"get": "retrieve", "put": "change", "delete": "delete"}
)

app_name = os.getcwd().split(os.sep)[-1]
urlpatterns = [
    path("", BASE_ENDPOINT),
    path("<int:pk>", PK_ENDPOINT),
    path("getTree", OrganizationViewSet.as_view({"get": "getTree"})),
    path("getTree/", OrganizationViewSet.as_view({"get": "getTree"}))
]
