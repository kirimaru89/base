import os
from django.urls import path
from .views.crud import NewsViewSet


BASE_ENDPOINT = NewsViewSet.as_view(
    {"get": "list", "post": "add", "delete": "delete_list"}
)

PK_ENDPOINT = NewsViewSet.as_view(
    {"get": "retrieve", "put": "change", "delete": "delete"}
)

app_name = os.getcwd().split(os.sep)[-1]
urlpatterns = [
    path("", BASE_ENDPOINT),
    path("<int:pk>", PK_ENDPOINT),
    path("<int:pk>/inactivate", NewsViewSet.as_view({"post":"inactivate"})),
    path("<int:pk>/activate", NewsViewSet.as_view({"post":"activate"})),
]
