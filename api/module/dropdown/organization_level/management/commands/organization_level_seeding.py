from django.core.management.base import BaseCommand

from module.dropdown.organization_level.models import OrganizationLevel


class Command(BaseCommand):
    help = "organization_level_seeding"

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Start..."))
        OrganizationLevel.objects.all().delete()
        self.seeding_data()

        self.stdout.write(self.style.SUCCESS("Done!!!"))

    def seeding_data(self):
        data = [
            "Quận (và tương đương)",
            "Đoàn giao quyền cấp trên cơ sở",
            "Đoàn cơ sở",
            "Chi đoàn cơ sở",
            "Liên chi đoàn",
            "Chi đoàn",
        ]
        for item in data:
            self.create_item(item)

    def create_item(self, data):
        OrganizationLevel.objects.create(
            name=data
        )
