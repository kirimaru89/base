from django.db import transaction
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from service.framework.drf_class.custom_permission import CustomPermission
from service.request_service import RequestService
from ..models import Campaign
from ..helper.sr import CampaignSr, CampaignListSr, CampaignDetailSr
from module.activity.campaign.consts import CAMPAIGN_TYPES
from module.dropdown.consts import BENEFICIARY_TYPES
from ...campaign_attachment.helper.util import CampaignAttachmentUtil
from ..helper.filter import CampaignFilter


class CampaignViewSet(GenericViewSet):
    _name = "campaign"
    serializer_class = CampaignSr
    # permission_classes = (CustomPermission,)
    filterset_class = CampaignFilter
    search_fields = ("title",)

    permission_classes=[AllowAny]
    def list(self, request):
        queryset = Campaign.objects.all()
        queryset = self.filter_queryset(queryset)
        queryset = self.paginate_queryset(queryset)
        serializer = CampaignListSr(queryset, many=True)
        
        options = {}
        options["beneficiaries"] = BENEFICIARY_TYPES    
        options["types"] = CAMPAIGN_TYPES
        
        result = {
            "items": serializer.data, 
            "extra": {
                "options": options
            }
        }
        
        return self.get_paginated_response(result)

    permission_classes=[AllowAny]
    def retrieve(self, request, pk=None):
        obj = get_object_or_404(Campaign, pk=pk)
        serializer = CampaignDetailSr(obj)
        
        return RequestService.res(serializer.data)
    
    @action(methods=["post"], detail=True)
    def add(self, request):
        data = request.data
        staff = request.user.staff
        data["created_by"] = staff.id
        data["updated_by"] = staff.id
        serializer = CampaignSr(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return RequestService.res(serializer.data)

    @transaction.atomic
    @action(methods=["put"], detail=True)
    def change(self, request, pk=None):
        obj = get_object_or_404(Campaign, pk=pk)
        data = request.data

        data["updated_by"] = request.user.staff.id
        serializer = CampaignSr(obj, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        images = data.get("images", [])
        files = data.get("files", [])
        attachments = images + files
        CampaignAttachmentUtil.update_attachment(attachments, obj)

        return RequestService.res(serializer.data)

    @action(methods=["delete"], detail=True)
    def delete(self, request, pk=None):
        obj = get_object_or_404(Campaign, pk=pk)
        obj.delete()
        return RequestService.res(status=status.HTTP_204_NO_CONTENT)

    @transaction.atomic
    @action(methods=["delete"], detail=False)
    def delete_list(self, request):
        pk = self.request.query_params.get("ids", "")
        pks = [int(pk)] if pk.isdigit() else [int(i) for i in pk.split(",")]
        for pk in pks:
            item = get_object_or_404(Campaign, pk=pk)
            item.delete()
        return RequestService.res(status=status.HTTP_204_NO_CONTENT)
