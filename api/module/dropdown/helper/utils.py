from module.account.union_member.consts import GENDER_CHOICES
from module.dropdown.education_level.helper.srs import EducationLevelSr
from module.dropdown.education_level.models import EducationLevel
from module.dropdown.ethnic.helper.srs import EthnicSr
from module.dropdown.ethnic.models import Ethnic
from module.dropdown.foreign_language_level.helper.srs import ForeignLanguageLevelSr
from module.dropdown.foreign_language_level.models import ForeignLanguageLevel
from module.dropdown.it_level.helper.srs import ItLevelSr
from module.dropdown.it_level.models import ItLevel
from module.dropdown.occupation.helper.srs import OccupationSr
from module.dropdown.occupation.models import Occupation
from module.dropdown.organization_level.helper.srs import OrganizationLevelSr
from module.dropdown.organization_level.models import OrganizationLevel
from module.dropdown.organization_type.helper.srs import OrganizationTypeSr
from module.dropdown.organization_type.models import OrganizationType
from module.dropdown.political_theory_level.helper.srs import PoliticalTheoryLevelSr
from module.dropdown.political_theory_level.models import PoliticalTheoryLevel
from module.dropdown.position.helper.srs import PositionSr
from module.dropdown.position.models import Position
from module.dropdown.qualification.helper.srs import QualificationSr
from module.dropdown.qualification.models import Qualification
from module.dropdown.recipient.helper.sr import RecipientOptionSr
from module.dropdown.recipient.models import Recipient
from module.dropdown.religion.helper.srs import ReligionSr
from module.dropdown.religion.models import Religion


class DropdownUtils:
    @staticmethod
    def get_gender():
        return [dict(id=value, name=label) for value, label in GENDER_CHOICES]

    @staticmethod
    def get_recipient():
        return RecipientOptionSr(Recipient.objects.all(), many=True).data

    @staticmethod
    def get_position():
        return PositionSr(Position.objects.all(), many=True).data

    @staticmethod
    def get_ethnic():
        return EthnicSr(Ethnic.objects.all(), many=True).data

    @staticmethod
    def get_religion():
        return ReligionSr(Religion.objects.all(), many=True).data

    @staticmethod
    def get_occupation():
        return OccupationSr(Occupation.objects.all(), many=True).data

    @staticmethod
    def get_education_level():
        return EducationLevelSr(EducationLevel.objects.all(), many=True).data

    @staticmethod
    def get_qualification():
        return QualificationSr(Qualification.objects.all(), many=True).data

    @staticmethod
    def get_it_level():
        return ItLevelSr(ItLevel.objects.all(), many=True).data

    @staticmethod
    def get_foreign_language_level():
        return ForeignLanguageLevelSr(
            ForeignLanguageLevel.objects.all(), many=True
        ).data

    @staticmethod
    def get_political_theory_level():
        return PoliticalTheoryLevelSr(
            PoliticalTheoryLevel.objects.all(), many=True
        ).data

    @staticmethod
    def get_organization_level():
        return OrganizationLevelSr(
            OrganizationLevel.objects.all(), many=True
        ).data

    @staticmethod
    def get_organization_type():
        return OrganizationTypeSr(
            OrganizationType.objects.all(), many=True
        ).data

    @staticmethod
    def get_options(user=None, lang="vi"):
        return dict(
            gender=DropdownUtils.get_gender(),
            recipient=DropdownUtils.get_recipient(),
            position=DropdownUtils.get_position(),
            ethnic=DropdownUtils.get_ethnic(),
            religion=DropdownUtils.get_religion(),
            occupation=DropdownUtils.get_occupation(),
            education_level=DropdownUtils.get_education_level(),
            qualification=DropdownUtils.get_qualification(),
            it_level=DropdownUtils.get_it_level(),
            foreign_language_level=DropdownUtils.get_foreign_language_level(),
            political_theory_level=DropdownUtils.get_political_theory_level(),
            organization_level=DropdownUtils.get_political_theory_level(),
            organization_type=DropdownUtils.get_political_theory_level(),
        )
