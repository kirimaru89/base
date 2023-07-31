from django.db import transaction
from django.shortcuts import get_object_or_404
from module.dropdown.organization.helper.util import OrganizationUtil
from module.dropdown.helper.util import DropdownUtil
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework import status
from service.framework.drf_class.custom_permission import CustomPermission

from service.request_service import RequestService
from ..models import Member
from ..helper.util import MemberUtil
from ..helper.sr import MemberDetailSr, MemberSr, MemberListSr


class MemberViewSet(GenericViewSet):

    _name = "member"
    permission_classes = (CustomPermission,)
    serializer_class = MemberSr
    search_fields = (
        "user__email",
        "user__mobile",
        "user__first_name",
        "user__last_name",
    )

    def list(self, request):
        queryset = Member.objects.all()
        queryset = self.filter_queryset(queryset)
        queryset = self.paginate_queryset(queryset)
        serializer = MemberListSr(queryset, many=True)

        options = DropdownUtil.get_options(user=request.user)
        organization_tree = OrganizationUtil.get_organization_tree()
        options["organization_tree"] = organization_tree

        result = {
            "items": serializer.data,
            "extra": {"options": options},
        }

        return self.get_paginated_response(result)

    def retrieve(self, request, pk=None):
        obj = get_object_or_404(Member, pk=pk)
        serializer = MemberDetailSr(obj)
        return RequestService.res(serializer.data)

    @transaction.atomic
    @action(methods=["post"], detail=True)
    def add(self, request):
        obj = MemberUtil.create_member(request.data)
        sr = MemberSr(obj)
        return RequestService.res(sr.data)

    @transaction.atomic
    @action(methods=["put"], detail=True)
    def change(self, request, pk=None):
        obj = get_object_or_404(Member, pk=pk)
        obj = MemberUtil.update_member(obj, request.data)
        sr = MemberSr(obj)
        return RequestService.res(sr.data)

    @transaction.atomic
    @action(methods=["delete"], detail=True)
    def delete(self, request, pk=None):
        item = get_object_or_404(Member, pk=pk)
        item.delete()
        return RequestService.res(status=status.HTTP_204_NO_CONTENT)

    @transaction.atomic
    @action(methods=["delete"], detail=False)
    def delete_list(self, request):
        pk = self.request.query_params.get("ids", "")
        pks = [int(pk)] if pk.isdigit() else [int(i) for i in pk.split(",")]
        for pk in pks:
            item = get_object_or_404(Member, pk=pk)
            item.delete()
        return RequestService.res(status=status.HTTP_204_NO_CONTENT)
