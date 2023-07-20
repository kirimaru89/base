import json
import copy
from django.core.management.base import BaseCommand
from django.conf import settings

from module.activities_place.models import ActivitiesPlace


class Command(BaseCommand):
    help = "activities_place_seeding"

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Start..."))
        ActivitiesPlace.objects.all().delete()
        self.seeding_data()

        self.stdout.write(self.style.SUCCESS("Done!!!"))

    def get_import_file_path(self, filename):
        print(type(settings.BASE_DIR))
        return "/".join(
            [
                str(settings.BASE_DIR),
                "module/activities_place/management/commands/import_data",
                filename,
            ]
        )

    def seeding_data(self):
        filename = "data.json"
        with open(self.get_import_file_path(filename), "r") as f:
            print("Import data...")
            list_item = json.load(f)
            for item in list_item:
                self.create_item(item)

    def create_item(self, data, parent=None, level=1, parent_ids=[]):
        print(data["name"])
        item = ActivitiesPlace.objects.create(
            parent=parent,
            name=data["name"],
            level_id=data["level"],
            parent_ids=parent_ids,
        )
        if data.get("children"):
            new_parent_ids = copy.deepcopy(parent_ids) + [item.pk]
            for data in data.get("children"):
                self.create_item(data, item, level, new_parent_ids)
