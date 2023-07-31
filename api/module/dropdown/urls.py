import os
from django.urls import path, include

app_name = os.getcwd().split(os.sep)[-1]

urlpatterns = (
    path(
        "recipient/",
        include("module.dropdown.recipient.urls", namespace="recipient"),
    ),
    path(
        "organization/",
        include("module.dropdown.organization.urls", namespace="organization"),
    ),
)
