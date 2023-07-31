from rest_framework.viewsets import GenericViewSet

from service.framework.drf_class.custom_pagination import NoPaginationStatic
from service.framework.drf_class.custom_permission import CustomPermission

from .helper.util import ReportUtil


class ReportViewSet(GenericViewSet):
    _name="report"
    permission_classes = (CustomPermission,)
    pagination_class = None

    def list(self, request):
        result = {
            "items": ReportUtil.get_report(),
        }
        return NoPaginationStatic.get_paginated_response(result)
