import os
from django.urls import path, include

app_name = os.getcwd().split(os.sep)[-1]

urlpatterns = (
    path("noti/", include("module.noti.urls", namespace="noti")),
    path("account/", include("module.account.urls", namespace="account")),
    path(
        "conf/",
        include("module.conf.urls", namespace="configuration"),
    ),
    path(
        "dropdown/",
        include("module.dropdown.urls", namespace="dropdown"),
    ),
    path("article/", include("module.article.urls", namespace="article")),
    path("management/", include("module.management.urls", namespace="management")),
    path(
        "activity/",
        include("module.activity.urls", namespace="activity"),
    ),
    path("report/", include("module.report.urls", namespace="report")),
)
