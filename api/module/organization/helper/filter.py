from django_filters import rest_framework as filters

from module.organization.models import Organization


class OrganizationFilter(filters.FilterSet):
    level = filters.NumberFilter(field_name="level")

    class Meta:
        model = Organization
        fields = [
            "level"
        ]
