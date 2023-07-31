from module.dropdown.occupation.models import Occupation
from module.dropdown.occupation.helper.sr import OccupationOptionSr
from module.dropdown.position.helper.sr import PositionOptionSr
from module.dropdown.position.models import Position
from module.noti.message.consts import SOURCE_TYPES
from module.activity.question.consts import QUESTION_TYPES
from module.dropdown.organization.consts import (
    ORGANIZATION_TYPES,
    ORGANIZATION_LEVELS,
)
from module.article.news.consts import NEWS_TYPES
from module.activity.campaign.consts import (
    CAMPAIGN_TYPES,
    BENEFICIARY_TYPES,
)
from module.activity.campaign_attachment.consts import (
    CAMPAIGN_ATTACHMENT_TYPES,
)
from module.account.member.consts import (
    ETHNICS,
    POLITICAL_THEORY_LEVELS,
    FOREIGN_LANGUAGE_LEVELS,
    IT_LEVELS,
    QUALIFICATIONS,
    EDUCATION_LEVELS,
    RELIGIONS,
    GENDERS,
)


class DropdownUtil:
    @staticmethod
    def get_position():
        return PositionOptionSr(Position.objects.all(), many=True).data

    @staticmethod
    def get_occupation():
        return OccupationOptionSr(Occupation.objects.all(), many=True).data

    @staticmethod
    def get_member_options():
        return dict(
            position=DropdownUtil.get_position(),
            occupation=DropdownUtil.get_occupation(),
            gender=GENDERS,
            ethnic=ETHNICS,
            religion=RELIGIONS,
            education_level=EDUCATION_LEVELS,
            qualification=QUALIFICATIONS,
            it_level=IT_LEVELS,
            foreign_language_level=FOREIGN_LANGUAGE_LEVELS,
            political_theory_level=POLITICAL_THEORY_LEVELS,
        )

    @staticmethod
    def get_options(user=None, lang="vi"):
        return dict(
            position=DropdownUtil.get_position(),
            occupation=DropdownUtil.get_occupation(),
            source_type=SOURCE_TYPES,
            question_type=QUESTION_TYPES,
            gender=GENDERS,
            beneficiary=BENEFICIARY_TYPES,
            ethnic=ETHNICS,
            religion=RELIGIONS,
            education_level=EDUCATION_LEVELS,
            qualification=QUALIFICATIONS,
            it_level=IT_LEVELS,
            foreign_language_level=FOREIGN_LANGUAGE_LEVELS,
            political_theory_level=POLITICAL_THEORY_LEVELS,
            organization_level=ORGANIZATION_LEVELS,
            organization_type=ORGANIZATION_TYPES,
            news_type=NEWS_TYPES,
            campaign_type=CAMPAIGN_TYPES,
            campaign_attachment_type=CAMPAIGN_ATTACHMENT_TYPES,
        )
