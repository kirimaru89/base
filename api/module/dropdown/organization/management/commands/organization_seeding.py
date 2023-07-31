import json
import copy
from django.core.management.base import BaseCommand
from django.conf import settings

from module.dropdown.organization.models import Organization


class Command(BaseCommand):
    help = "organization_seeding"

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Start..."))
        Organization.objects.all().delete()
        self.seeding_data()

        self.stdout.write(self.style.SUCCESS("Done!!!"))

    def get_import_file_path(self, filename):
        return "/".join(
            [
                str(settings.BASE_DIR),
                "module/dropdown/organization/management/commands/import_data",
                filename,
            ]
        )

    def seeding_data(self):
        filename = "data.json"
        with open(self.get_import_file_path(filename), "r") as f:
            print("Import data...")
            list_item = json.load(f)
            print(list_item)
            for item in list_item:
                self.create_item(item)

    def create_item(self, data, parent=None, parent_ids=[]):
        print(data["title"])
        item = Organization.objects.create(
            parent=parent,
            title=data["title"],
            type=data["type"],
            level=data["level"],
            parent_ids=parent_ids,
        )
        if data.get("children"):
            new_parent_ids = copy.deepcopy(parent_ids) + [item.pk]
            for data in data.get("children"):
                self.create_item(data, item, new_parent_ids)
