import os
from django.urls import path
from .views.crud import MediaViewSet

app_name = os.getcwd().split(os.sep)[-1]
urlpatterns = [
    path("upload-image", MediaViewSet.as_view(), name="upload_image")
]
