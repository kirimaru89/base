from datetime import timedelta
from django.db import transaction
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet
from rest_framework import status
from service.framework.drf_class.custom_permission import CustomPermission
from service.date_service import DateService
from service.request_service import RequestService
from module.activity.contest.models import Contest
from module.activity.exam.helper.util import ExamUtil
from ..models import Exam
from ..helper.sr import ExamSr


class ExamViewSet(GenericViewSet):
    _name = "exam"
    serializer_class = ExamSr
    permission_classes = (CustomPermission,)
    search_fields = ("title",)

    def list(self, request):
        queryset = Exam.objects.all()
        queryset = self.filter_queryset(queryset)
        queryset = self.paginate_queryset(queryset)
        serializer = ExamSr(queryset, many=True)
        return self.get_paginated_response(serializer.data)

    def retrieve(self, request, pk=None):
        obj = get_object_or_404(Exam, pk=pk)
        serializer = ExamSr(obj)
        return RequestService.res(serializer.data)

    @action(methods=["post"], detail=True)
    def add(self, request):
        data = request.data
        contest = data.get("contest")
        contest = get_object_or_404(Contest, pk=contest)
        duration = contest.duration
        data["member"] = request.user.member.pk
        data["started_at"] = DateService.now()
        data["finished_at"] = DateService.now() + timedelta(minutes=duration)
        serializer = ExamSr(data=request.data)
        serializer.is_valid(raise_exception=True)
        obj = serializer.save()
        ExamUtil.clone_exam_questions(obj)
        obj = Exam.objects.get(pk=obj.pk)
        serializer = ExamSr(obj)

        return RequestService.res(serializer.data)

    @action(methods=["delete"], detail=True)
    def delete(self, request, pk=None):
        obj = get_object_or_404(Exam, pk=pk)
        obj.delete()
        return RequestService.res(status=status.HTTP_204_NO_CONTENT)

    @transaction.atomic
    @action(methods=["delete"], detail=False)
    def delete_list(self, request):
        pk = self.request.query_params.get("ids", "")
        pks = [int(pk)] if pk.isdigit() else [int(i) for i in pk.split(",")]
        for pk in pks:
            item = get_object_or_404(Exam, pk=pk)
            item.delete()
        return RequestService.res(status=status.HTTP_204_NO_CONTENT)
