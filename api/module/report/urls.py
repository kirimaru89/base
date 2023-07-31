import os
from django.urls import path

from module.report.views import ReportViewSet

BASE_ENDPOINT = ReportViewSet.as_view({"get": "list"})

app_name = os.getcwd().split(os.sep)[-1]
urlpatterns = [
    path("", BASE_ENDPOINT),
]
