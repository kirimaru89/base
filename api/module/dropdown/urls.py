import os
from django.urls import path, include

app_name = os.getcwd().split(os.sep)[-1]

urlpatterns = (
    path(
        "recipient/",
        include("module.dropdown.recipient.urls", namespace="recipient"),
    ),
    path(
        "newsType/",
        include("module.dropdown.newsType.urls", namespace="newsType"),
    ),
    path(
        "position/",
        include("module.dropdown.position.urls", namespace="position"),
    ),
    path(
        "ethnic/",
        include("module.dropdown.ethnic.urls", namespace="ethnic"),
    ),
    path(
        "religion/",
        include("module.dropdown.religion.urls", namespace="religion"),
    ),
    path(
        "occupation/",
        include("module.dropdown.occupation.urls", namespace="occupation"),
    ),
    path(
        "education_level/",
        include("module.dropdown.education_level.urls", namespace="education_level"),
    ),
    path(
        "qualification/",
        include("module.dropdown.qualification.urls", namespace="qualification"),
    ),
    path(
        "it_level/",
        include("module.dropdown.it_level.urls", namespace="it_level"),
    ),
    path(
        "foreign_language_level/",
        include("module.dropdown.foreign_language_level.urls", namespace="foreign_language_level"),
    ),
    path(
        "political_theory_level/",
        include("module.dropdown.political_theory_level.urls", namespace="political_theory_level"),
    ),
)
