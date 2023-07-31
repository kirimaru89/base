import os
from django.urls import path
from .views.crud import FileViewSet

app_name = os.getcwd().split(os.sep)[-1]
urlpatterns = [
    path("upload", FileViewSet.as_view(), name="upload")
]
