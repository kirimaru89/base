import os
from django.urls import path

from module.account.union_member.views.crud import UnionMemberViewSet
from module.account.union_member.views.profile import ProfileView

BASE_ENDPOINT = UnionMemberViewSet.as_view(
    {"get": "list", "post": "add", "delete": "delete_list"}
)

PK_ENDPOINT = UnionMemberViewSet.as_view(
    {"get": "retrieve", "put": "change", "delete": "delete"}
)


app_name = os.getcwd().split(os.sep)[-1]
urlpatterns = [
    path("", BASE_ENDPOINT),
    path("<int:pk>", PK_ENDPOINT),
    path("profile/", ProfileView.as_view(), name="profile"),
]
