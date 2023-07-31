from django.db import transaction
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet
from rest_framework import status
from service.framework.drf_class.custom_permission import CustomPermission
from service.request_service import RequestService
from ..helper.filter import ContestFilter
from ..models import Contest
from ..helper.sr import ContestSr


class ContestViewSet(GenericViewSet):
    _name = "contest"
    serializer_class = ContestSr
    permission_classes = (CustomPermission,)
    filterset_class = ContestFilter
    search_fields = ("title",)

    def list(self, request):
        member = request.user.member if hasattr(request.user, 'member') else {}
        
        queryset = Contest.objects.all()
        queryset = self.filter_queryset(queryset)
        queryset = self.paginate_queryset(queryset)
        serializer = ContestSr(queryset, many=True, context={"member": member})
        return self.get_paginated_response(serializer.data)

    def retrieve(self, request, pk=None):
        obj = get_object_or_404(Contest, pk=pk)
        member = request.user.member if hasattr(request.user, 'member') else {}
        
        serializer = ContestSr(obj, context={"member": member})
        return RequestService.res(serializer.data)

    @action(methods=["post"], detail=True)
    def add(self, request):
        data = request.data
        data["created_by"] = request.user.staff.pk
        data["updated_by"] = request.user.staff.pk
        serializer = ContestSr(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return RequestService.res(serializer.data)

    @action(methods=["put"], detail=True)
    def change(self, request, pk=None):
        data = request.data
        data["updated_by"] = request.user.staff.pk
        obj = get_object_or_404(Contest, pk=pk)
        serializer = ContestSr(obj, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return RequestService.res(serializer.data)

    @action(methods=["delete"], detail=True)
    def delete(self, request, pk=None):
        obj = get_object_or_404(Contest, pk=pk)
        obj.delete()
        return RequestService.res(status=status.HTTP_204_NO_CONTENT)

    @transaction.atomic
    @action(methods=["delete"], detail=False)
    def delete_list(self, request):
        pk = self.request.query_params.get("ids", "")
        pks = [int(pk)] if pk.isdigit() else [int(i) for i in pk.split(",")]
        for pk in pks:
            item = get_object_or_404(Contest, pk=pk)
            item.delete()
        return RequestService.res(status=status.HTTP_204_NO_CONTENT)
