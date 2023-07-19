from django.core.management.base import BaseCommand

from module.dropdown.occupation.models import Occupation


class Command(BaseCommand):
    help = "occupation_seeding"

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Start..."))
        Occupation.objects.all().delete()
        self.seeding_data()

        self.stdout.write(self.style.SUCCESS("Done!!!"))

    def seeding_data(self):
        data = [
            "Học sinh",
            "Giáo viên",
            "Công an",
            "Kế toán",
            "Kiểm toán",
            "Kỹ sư",
            "Kiến trúc sư",
            "Nhà báo",
        ]
        for item in data:
            self.create_item(item)

    def create_item(self, data):
        Occupation.objects.create(
            name=data
        )
