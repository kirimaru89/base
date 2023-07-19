from django.core.management.base import BaseCommand

from module.dropdown.foreign_language_level.models import ForeignLanguageLevel


class Command(BaseCommand):
    help = "foreign_language_level_seeding"

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Start..."))
        ForeignLanguageLevel.objects.all().delete()
        self.seeding_data()

        self.stdout.write(self.style.SUCCESS("Done!!!"))

    def seeding_data(self):
        data = [
            "Bậc 1",
            "Bậc 2",
            "Bậc 3",
        ]
        for item in data:
            self.create_item(item)

    def create_item(self, data):
        ForeignLanguageLevel.objects.create(
            name=data
        )
