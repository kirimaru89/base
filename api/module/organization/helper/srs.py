from rest_framework.serializers import ModelSerializer

from module.organization.models import Organization


class OrganizationSr(ModelSerializer):
    class Meta:
        model = Organization
        exclude = ()
