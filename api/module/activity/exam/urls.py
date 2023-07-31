import os
from django.urls import path
from .views.crud import ExamViewSet
from .views.custom import SubmitView


BASE_ENDPOINT = ExamViewSet.as_view(
    {"get": "list", "post": "add", "delete": "delete_list"}
)

PK_ENDPOINT = ExamViewSet.as_view({"get": "retrieve", "delete": "delete"})

app_name = os.getcwd().split(os.sep)[-1]
urlpatterns = [
    path("", BASE_ENDPOINT),
    path("<int:pk>", PK_ENDPOINT),
    path("submit/<int:pk>", SubmitView.as_view({"put": "submit"})),
    path("detail/<int:pk>", SubmitView.as_view({"get": "retrieve"})),
]
