from django.core.management.base import BaseCommand

from module.dropdown.organization.consts import OrganizationLevel
from module.dropdown.organization.models import Organization


class Command(BaseCommand):
    help = "cmd_update_parent_ids"

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Start..."))

        organizations = Organization.objects.all()
        root_parent = Organization.objects.filter(level=OrganizationLevel.CITY)
        if root_parent:
            root_id = root_parent.first().id
            organizations.update(root_parent=root_id)

        for item in organizations:
            self.update_parents(organizations, item)

        self.stdout.write(self.style.SUCCESS("Done!!!"))

    def update_parents(self, data, item):
        parent = item.parent
        if not parent:
            item.parent_ids = []
            item.save()
        else:
            for d in data:
                if d.id == parent.id:
                    if not d.parent_ids:
                        self.update_parents(data, d)
                    item.parent_ids = d.parent_ids + [d.id]
                    item.save()
                    break
