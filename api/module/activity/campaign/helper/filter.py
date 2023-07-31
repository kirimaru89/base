from django_filters import rest_framework as filters
from service.date_service import DateService
from ..models import Campaign
from ..consts import CampaignStatus


class CampaignFilter(filters.FilterSet):
    status = filters.NumberFilter(field_name="status", method="filter_status")
    beneficiary_types = filters.CharFilter(lookup_expr='icontains')
    
    def filter_status(self, queryset, _name, value):
        if not value:
            return queryset
        
        return queryset.filter(status=value)
        # if value == CampaignStatus.NOT_STARTED:
        #     return queryset.filter(start_at__gt=DateService.now())
        # if value == CampaignStatus.FINISHED:
        #     return queryset.filter(end_at__lt=DateService.now())
        # if value == CampaignStatus.STARTED:
        #     return queryset.filter(
        #         start_at__lte=DateService.now(), end_at__gte=DateService.now()
        #     )
        # return queryset

    class Meta:
        model = Campaign
        exclude = ()
