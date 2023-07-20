from django.core.management.base import BaseCommand

from module.dropdown.organization_type.models import OrganizationType


class Command(BaseCommand):
    help = "organization_type_seeding"

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Start..."))
        OrganizationType.objects.all().delete()
        self.seeding_data()

        self.stdout.write(self.style.SUCCESS("Done!!!"))

    def seeding_data(self):
        data = [
            "Khối doanh nghiệp nhà nước",
            "Khối doanh nghiệp ngoài nhà nước",
            "Khối công chức, viên chức",
            "Khối lực lượng, vũ trang",
            "Khối trường học",
            "Khối đô thị",
            "Khối nông thôn",
            "Khối cơ quan và doanh nghiệp",
        ]
        for item in data:
            self.create_item(item)

    def create_item(self, data):
        OrganizationType.objects.create(
            name=data
        )
