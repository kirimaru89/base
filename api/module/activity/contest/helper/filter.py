from django_filters import rest_framework as filters
from service.date_service import DateService
from ..models import Contest
from ..consts import ContestStatus


class ContestFilter(filters.FilterSet):
    status = filters.NumberFilter(field_name="status", method="filter_status")

    def filter_status(self, queryset, _name, value):
        if not value:
            return queryset
        if value == ContestStatus.NOT_STARTED:
            return queryset.filter(start_at__gt=DateService.now())
        if value == ContestStatus.FINISHED:
            return queryset.filter(end_at__lt=DateService.now())
        if value == ContestStatus.STARTED:
            return queryset.filter(
                start_at__lte=DateService.now(), end_at__gte=DateService.now()
            )
        return queryset

    class Meta:
        model = Contest
        exclude = ()
