from module.dropdown.organization.models import Organization
from module.dropdown.organization.helper.sr import OrganizationTreeSr


class OrganizationUtil:
    @staticmethod
    def get_organization_tree():
        queryset = Organization.objects.filter(root_parent__isnull=True).order_by(
            "title"
        )
        return OrganizationTreeSr(queryset, many=True).data
