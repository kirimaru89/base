from module.account.member.models import Member
from module.activity.campaign.models import Campaign
from module.activity.contest.models import Contest
from module.dropdown.organization.consts import OrganizationLevel
from module.dropdown.organization.models import Organization


class ReportUtil:
    @staticmethod
    def get_report():
        return dict(
            organization=Organization.objects.count(),
            member=Member.objects.all().count(),
            campaign=Campaign.objects.all().count(),
            contest=Contest.objects.all().count(),
        )
