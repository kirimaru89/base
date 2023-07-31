import os
from django.urls import path
from .views.crud import CampaignAttachmentViewSet


BASE_ENDPOINT = CampaignAttachmentViewSet.as_view(
    {"get": "list", "post": "add", "delete": "delete_list"}
)

PK_ENDPOINT = CampaignAttachmentViewSet.as_view(
    {"get": "retrieve", "put": "change", "delete": "delete"}
)

app_name = os.getcwd().split(os.sep)[-1]
urlpatterns = [
    path("", BASE_ENDPOINT),
    path("<int:pk>", PK_ENDPOINT),
]
