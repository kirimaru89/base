from django.db import transaction
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet
from rest_framework import status
from service.framework.drf_class.custom_permission import CustomPermission
from service.request_service import RequestService
from ..models import ExamAnswer
from ..helper.sr import ExamAnswerSr


class ExamAnswerViewSet(GenericViewSet):
    _name = "exam_answer"
    serializer_class = ExamAnswerSr
    permission_classes = (CustomPermission,)
    search_fields = ("title",)

    def list(self, request):
        queryset = ExamAnswer.objects.all()
        queryset = self.filter_queryset(queryset)
        queryset = self.paginate_queryset(queryset)
        serializer = ExamAnswerSr(queryset, many=True)
        return self.get_paginated_response(serializer.data)

    def retrieve(self, request, pk=None):
        obj = get_object_or_404(ExamAnswer, pk=pk)
        serializer = ExamAnswerSr(obj)
        return RequestService.res(serializer.data)

    @action(methods=["post"], detail=True)
    def add(self, request):
        serializer = ExamAnswerSr(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return RequestService.res(serializer.data)

    @action(methods=["put"], detail=True)
    def change(self, request, pk=None):
        obj = get_object_or_404(ExamAnswer, pk=pk)
        serializer = ExamAnswerSr(obj, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return RequestService.res(serializer.data)

    @action(methods=["delete"], detail=True)
    def delete(self, request, pk=None):
        obj = get_object_or_404(ExamAnswer, pk=pk)
        obj.delete()
        return RequestService.res(status=status.HTTP_204_NO_CONTENT)

    @transaction.atomic
    @action(methods=["delete"], detail=False)
    def delete_list(self, request):
        pk = self.request.query_params.get("ids", "")
        pks = [int(pk)] if pk.isdigit() else [int(i) for i in pk.split(",")]
        for pk in pks:
            item = get_object_or_404(ExamAnswer, pk=pk)
            item.delete()
        return RequestService.res(status=status.HTTP_204_NO_CONTENT)
