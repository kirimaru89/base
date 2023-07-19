from django.core.management.base import BaseCommand

from module.dropdown.qualification.models import Qualification


class Command(BaseCommand):
    help = "qualification_seeding"

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Start..."))
        Qualification.objects.all().delete()
        self.seeding_data()

        self.stdout.write(self.style.SUCCESS("Done!!!"))

    def seeding_data(self):
        data = [
            "Tiến sĩ",
            "Thạc sĩ",
            "Cao đẳng",
            "Trung cấp",
            "Sơ cấp",
        ]
        for item in data:
            self.create_item(item)

    def create_item(self, data):
        Qualification.objects.create(
            name=data
        )
