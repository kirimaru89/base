from django.db import transaction
from django.shortcuts import get_object_or_404
from module.organization.helper.util import OrganizationUtil
from module.dropdown.helper.utils import DropdownUtils
from rest_framework import status
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action

from module.account.union_member.helper.sr import UnionMemberSr, UnionMemberDetailSr, ListUnionMemberSr
from module.account.union_member.helper.util import UnionMemberUtil
from module.account.union_member.models import UnionMember
from service.request_service import RequestService
from service.framework.drf_class.custom_permission import CustomPermission


class UnionMemberViewSet(GenericViewSet):
    _name = "unnion_member"
    permission_classes = (CustomPermission,)
    serializer_class = UnionMemberSr
    search_fields = (
        "user__email",
        "user__phone_number",
        "user__first_name",
        "user__last_name",
        "full_name",
    )

    def list(self, request):
        queryset = UnionMember.objects.all()
        queryset = self.filter_queryset(queryset)
        queryset = self.paginate_queryset(queryset)
        serializer = ListUnionMemberSr(queryset, many=True)

        organization_tree = OrganizationUtil.get_organization_tree()
        options = DropdownUtils.get_options(user=request.user)
        options["organization_tree"] = organization_tree
        
        result = {
            "items": serializer.data, 
            "extra": {
                "options": options
            }
        }
        return self.get_paginated_response(result)

    def retrieve(self, request, pk=None):
        obj = get_object_or_404(UnionMember, pk=pk)
        serializer = UnionMemberDetailSr(obj)
        return RequestService.res(serializer.data)

    @transaction.atomic
    @action(methods=["post"], detail=True)
    def add(self, request):
        group_id = 4 # đoàn viên
        data = request.data
        data["groups"] = [group_id]
        obj = UnionMemberUtil.create_union_member(data)
        sr = UnionMemberSr(obj)
        return RequestService.res(sr.data)

    @transaction.atomic
    @action(methods=["put"], detail=True)
    def change(self, request, pk=None):
        obj = get_object_or_404(UnionMember, pk=pk)
        obj = UnionMemberUtil.update_union_member(obj, request.data)
        sr = UnionMemberSr(obj)
        return RequestService.res(sr.data)

    @transaction.atomic
    @action(methods=["delete"], detail=True)
    def delete(self, request, pk=None):
        item = get_object_or_404(UnionMember, pk=pk)
        item.delete()
        return RequestService.res(status=status.HTTP_204_NO_CONTENT)

    @transaction.atomic
    @action(methods=["delete"], detail=False)
    def delete_list(self, request):
        pk = self.request.query_params.get("ids", "")
        pks = [int(pk)] if pk.isdigit() else [int(i) for i in pk.split(",")]
        for pk in pks:
            item = get_object_or_404(UnionMember, pk=pk)
            item.delete()
        return RequestService.res(status=status.HTTP_204_NO_CONTENT)
