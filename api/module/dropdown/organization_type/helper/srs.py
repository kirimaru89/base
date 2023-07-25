from rest_framework.serializers import ModelSerializer
from module.dropdown.organization_type.models import OrganizationType


class OrganizationTypeSr(ModelSerializer):
    class Meta:
        model = OrganizationType
        exclude = ()
