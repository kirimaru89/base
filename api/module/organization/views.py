from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import AllowAny

from module.organization.helper.filter import OrganizationFilter
from module.organization.helper.srs import OrganizationSr
from module.organization.models import Organization
from service.framework.drf_class.custom_pagination import NoPaginationStatic
from service.request_service import RequestService


class OrganizationListViewSet(GenericViewSet):
    filterset_class = OrganizationFilter
    permission_classes = (AllowAny,)
    search_fields = (
        "level"
    )

    def list(self, request):
        parent = request.query_params.get("parent") or None
        try:
            if parent is None:
                queryset = Organization.objects.filter(parent__id__isnull=True)
            else:
                queryset = Organization.objects.filter(parent__id=parent)
        except ValueError:
            return RequestService.res([])

        queryset = queryset.order_by("level", "id")
        sr = OrganizationSr(queryset, many=True)
        # return NoPaginationStatic.get_paginated_response(sr.data)
        return RequestService.res(sr.data)
