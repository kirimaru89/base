from django.core.management.base import BaseCommand

from module.dropdown.it_level.models import ItLevel


class Command(BaseCommand):
    help = "it_level_seeding"

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Start..."))
        ItLevel.objects.all().delete()
        self.seeding_data()

        self.stdout.write(self.style.SUCCESS("Done!!!"))

    def seeding_data(self):
        data = [
            "Chuẩn kỹ năng sử dụng CNTT cơ bản",
            "Chuẩn kỹ năng sử dụng CNTT nâng cao",
            "Không có",
        ]
        for item in data:
            self.create_item(item)

    def create_item(self, data):
        ItLevel.objects.create(
            name=data
        )
