import os
from django.urls import path, include

app_name = os.getcwd().split(os.sep)[-1]

urlpatterns = (
    path("campaign/", include("module.activity.campaign.urls", namespace="campaign")),
    path("campaign-attachment/", include("module.activity.campaign_attachment.urls", namespace="campaign_attachment")),
    path("contest/", include("module.activity.contest.urls", namespace="contest")),
    path("question/", include("module.activity.question.urls", namespace="question")),
    path("exam/", include("module.activity.exam.urls", namespace="exam")),
)
