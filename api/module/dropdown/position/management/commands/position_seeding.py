from django.core.management.base import BaseCommand

from module.dropdown.position.models import Position


class Command(BaseCommand):
    help = "position_seeding"

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Start..."))
        Position.objects.all().delete()
        self.seeding_data()

        self.stdout.write(self.style.SUCCESS("Done!!!"))

    def seeding_data(self):
        data = [
            "Đoàn viên",
            "Bí thư chi đoàn",
            "Phó bí thư chi đoàn",
            "UV Ban Chấp hành chi đoàn",
            "Bí thư đoàn cơ sở"
        ]
        for item in data:
            self.create_item(item)

    def create_item(self, data):
        Position.objects.create(
            name=data
        )
