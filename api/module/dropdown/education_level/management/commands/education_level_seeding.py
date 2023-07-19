from django.core.management.base import BaseCommand

from module.dropdown.education_level.models import EducationLevel


class Command(BaseCommand):
    help = "education_level_seeding"

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Start..."))
        EducationLevel.objects.all().delete()
        self.seeding_data()

        self.stdout.write(self.style.SUCCESS("Done!!!"))

    def seeding_data(self):
        data = [
            "Tiểu học",
            "Trung học cơ sở",
            "Trung học phổ thông hệ 10/10",
            "Trung học phổ thông hệ 12/12"
        ]
        for item in data:
            self.create_item(item)

    def create_item(self, data):
        EducationLevel.objects.create(
            name=data
        )
