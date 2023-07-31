import os
from django.urls import path
from .views.crud import MessageViewSet


BASE_ENDPOINT = MessageViewSet.as_view({"get": "list", "put": "mark_read"})

PK_ENDPOINT = MessageViewSet.as_view({"get": "retrieve"})

app_name = os.getcwd().split(os.sep)[-1]
urlpatterns = [
    path("", BASE_ENDPOINT),
    path("<int:pk>", PK_ENDPOINT),
]
