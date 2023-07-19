from django.core.management.base import BaseCommand

from module.dropdown.political_theory_level.models import PoliticalTheoryLevel


class Command(BaseCommand):
    help = "political_theory_level_seeding"

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Start..."))
        PoliticalTheoryLevel.objects.all().delete()
        self.seeding_data()

        self.stdout.write(self.style.SUCCESS("Done!!!"))

    def seeding_data(self):
        data = [
            "Cao cấp",
            "Trung cấp",
            "Sơ cấp",
            "Chưa có",
        ]
        for item in data:
            self.create_item(item)

    def create_item(self, data):
        PoliticalTheoryLevel.objects.create(
            name=data
        )
