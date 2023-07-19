from django.core.management.base import BaseCommand

from module.dropdown.ethnic.models import Ethnic


class Command(BaseCommand):
    help = "ethnic_seeding"

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Start..."))
        Ethnic.objects.all().delete()
        self.seeding_data()

        self.stdout.write(self.style.SUCCESS("Done!!!"))

    def seeding_data(self):
        data = [
            "Kinh",
            "Ê đê",
            "Tày",
            "Mường",
        ]
        for item in data:
            self.create_item(item)

    def create_item(self, data):
        Ethnic.objects.create(
            name=data
        )
