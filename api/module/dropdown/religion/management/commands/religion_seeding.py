from django.core.management.base import BaseCommand

from module.dropdown.religion.models import Religion


class Command(BaseCommand):
    help = "religion_seeding"

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Start..."))
        Religion.objects.all().delete()
        self.seeding_data()

        self.stdout.write(self.style.SUCCESS("Done!!!"))

    def seeding_data(self):
        data = [
            "Không",
            "Tin lành",
            "Công giáo",
        ]
        for item in data:
            self.create_item(item)

    def create_item(self, data):
        Religion.objects.create(
            name=data
        )
