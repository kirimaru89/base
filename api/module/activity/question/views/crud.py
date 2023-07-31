from django.db import transaction
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.serializers import ValidationError
from rest_framework.viewsets import GenericViewSet
from rest_framework import status
from service.framework.drf_class.custom_permission import CustomPermission
from service.request_service import RequestService
from module.activity.question.helper.util import QuestionUtil
from ..consts import QUESTION_TYPES
from ..models import Question
from ..helper.sr import QuestionSr


class QuestionViewSet(GenericViewSet):
    _name = "question"
    serializer_class = QuestionSr
    permission_classes = (CustomPermission,)
    search_fields = ("title",)

    def list(self, request):
        contest = request.query_params.get("contest")
        queryset = Question.objects.filter(contest=contest)
        queryset = self.filter_queryset(queryset)
        queryset = self.paginate_queryset(queryset)
        serializer = QuestionSr(queryset, many=True)

        options = {"type": QUESTION_TYPES}

        result = {
            "items": serializer.data,
            "extra": {"options": options},
        }

        return self.get_paginated_response(result)

    def retrieve(self, request, pk=None):
        obj = get_object_or_404(Question, pk=pk)
        serializer = QuestionSr(obj)
        return RequestService.res(serializer.data)

    @action(methods=["post"], detail=True)
    @transaction.atomic
    def add(self, request):
        question_type = request.data.get("type")
        answers = request.data.get("answers", [])
        serializer = QuestionSr(data=request.data)
        serializer.is_valid(raise_exception=True)
        obj = serializer.save()
        ok, msg = QuestionUtil.check_valid_answers(question_type, answers)
        if not ok:
            raise ValidationError({"detail": msg})
        QuestionUtil.clean_and_create_answers(obj, answers)
        return RequestService.res(serializer.data)

    @action(methods=["put"], detail=True)
    @transaction.atomic
    def change(self, request, pk=None):
        question_type = request.data.get("type")
        answers = request.data.get("answers", [])
        obj = get_object_or_404(Question, pk=pk)
        serializer = QuestionSr(obj, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        obj = serializer.save()
        ok, msg = QuestionUtil.check_valid_answers(question_type, answers)
        if not ok:
            raise ValidationError({"detail": msg})
        QuestionUtil.clean_and_create_answers(obj, answers)
        return RequestService.res(serializer.data)

    @action(methods=["delete"], detail=True)
    def delete(self, request, pk=None):
        obj = get_object_or_404(Question, pk=pk)
        obj.delete()
        return RequestService.res(status=status.HTTP_204_NO_CONTENT)

    @transaction.atomic
    @action(methods=["delete"], detail=False)
    def delete_list(self, request):
        pk = self.request.query_params.get("ids", "")
        pks = [int(pk)] if pk.isdigit() else [int(i) for i in pk.split(",")]
        for pk in pks:
            item = get_object_or_404(Question, pk=pk)
            item.delete()
        return RequestService.res(status=status.HTTP_204_NO_CONTENT)
