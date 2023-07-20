import os
from django.urls import path, include

from module.activities_place.views import ActivitiesPlaceListViewSet

app_name = os.getcwd().split(os.sep)[-1]

BASE_ENDPOINT = ActivitiesPlaceListViewSet.as_view({"get": "list"})

urlpatterns = (
    path("", BASE_ENDPOINT),
)
