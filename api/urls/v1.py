import os
from django.urls import path, include

app_name = os.getcwd().split(os.sep)[-1]

urlpatterns = (
    path("noti/", include("module.noti.urls", namespace="noti")),
    path("account/", include("module.account.urls", namespace="account")),
    path(
        "configuration/",
        include("module.conf.urls", namespace="configuration"),
    ),
    path(
        "dropdown/",
        include("module.dropdown.urls", namespace="dropdown"),
    ),
    path(
        "post/",
        include("module.post.urls", namespace="post"),
    ),
    path(
        "files/",
        include("module.files.urls", namespace="files"),
    ),
    path(
        "activities-place/",
        include("module.activities_place.urls", namespace="activities_place"),
    ),
)
