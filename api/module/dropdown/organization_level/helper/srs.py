from rest_framework.serializers import ModelSerializer
from module.dropdown.organization_level.models import OrganizationLevel


class OrganizationLevelSr(ModelSerializer):
    class Meta:
        model = OrganizationLevel
        exclude = ()
