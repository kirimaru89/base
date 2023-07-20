from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import AllowAny

from module.activities_place.helper.srs import ActivitiesPlaceSr
from module.activities_place.models import ActivitiesPlace
from service.framework.drf_class.custom_pagination import NoPaginationStatic
from service.request_service import RequestService


class ActivitiesPlaceListViewSet(GenericViewSet):
    permission_classes = (AllowAny,)

    def list(self, request):
        parent = request.query_params.get("parent") or None
        try:
            if parent is None:
                queryset = ActivitiesPlace.objects.filter(parent__id__isnull=True)
            else:
                queryset = ActivitiesPlace.objects.filter(parent__id=parent)
        except ValueError:
            return RequestService.res([])

        queryset = queryset.order_by("level", "id")
        sr = ActivitiesPlaceSr(queryset, many=True)
        # return NoPaginationStatic.get_paginated_response(sr.data)
        return RequestService.res(sr.data)
