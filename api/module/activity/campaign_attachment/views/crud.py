from django.db import transaction
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet
from rest_framework import status
from service.framework.drf_class.custom_permission import CustomPermission
from service.request_service import RequestService
from ..models import CampaignAttachment
from ..helper.sr import CampaignAttachmentSr


class CampaignAttachmentViewSet(GenericViewSet):
    _name = "campaign_attachment"
    serializer_class = CampaignAttachmentSr
    permission_classes = (CustomPermission,)
    search_fields = ("title",)

    def list(self, request):
        queryset = CampaignAttachment.objects.all()
        queryset = self.filter_queryset(queryset)
        queryset = self.paginate_queryset(queryset)
        serializer = CampaignAttachmentSr(queryset, many=True)
        return self.get_paginated_response(serializer.data)

    def retrieve(self, request, pk=None):
        obj = get_object_or_404(CampaignAttachment, pk=pk)
        serializer = CampaignAttachmentSr(obj)
        return RequestService.res(serializer.data)

    @action(methods=["post"], detail=True)
    def add(self, request):
        serializer = CampaignAttachmentSr(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return RequestService.res(serializer.data)

    @action(methods=["put"], detail=True)
    def change(self, request, pk=None):
        obj = get_object_or_404(CampaignAttachment, pk=pk)
        serializer = CampaignAttachmentSr(obj, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return RequestService.res(serializer.data)

    @action(methods=["delete"], detail=True)
    def delete(self, request, pk=None):
        obj = get_object_or_404(CampaignAttachment, pk=pk)
        obj.delete()
        return RequestService.res(status=status.HTTP_204_NO_CONTENT)

    @transaction.atomic
    @action(methods=["delete"], detail=False)
    def delete_list(self, request):
        pk = self.request.query_params.get("ids", "")
        pks = [int(pk)] if pk.isdigit() else [int(i) for i in pk.split(",")]
        for pk in pks:
            item = get_object_or_404(CampaignAttachment, pk=pk)
            item.delete()
        return RequestService.res(status=status.HTTP_204_NO_CONTENT)
