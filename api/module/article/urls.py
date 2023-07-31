import os
from django.urls import path, include

app_name = os.getcwd().split(os.sep)[-1]

urlpatterns = (
    path(
        "news/",
        include("module.article.news.urls", namespace="news"),
    ),
    path(
        "category/",
        include("module.article.category.urls", namespace="category"),
    ),
)
