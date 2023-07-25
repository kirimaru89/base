from rest_framework.serializers import ModelSerializer

from module.account.union_member.consts import GENDER_DICT
from module.account.union_member.models import UnionMember
from module.dropdown.education_level.helper.srs import EducationLevelSr
from module.dropdown.ethnic.helper.srs import EthnicSr
from module.dropdown.foreign_language_level.helper.srs import ForeignLanguageLevelSr
from module.dropdown.it_level.helper.srs import ItLevelSr
from module.dropdown.occupation.helper.srs import OccupationSr
from module.dropdown.political_theory_level.helper.srs import PoliticalTheoryLevelSr
from module.dropdown.position.helper.srs import PositionSr
from module.dropdown.qualification.helper.srs import QualificationSr
from module.dropdown.religion.helper.srs import ReligionSr


class UnionMemberSr(ModelSerializer):
    class Meta:
        model = UnionMember
        exclude = []

    def to_representation(self, obj):
        rep = super().to_representation(obj)
        user = obj.user
        rep["email"] = user.email
        rep["phone_number"] = str(user.phone_number)
        return rep

class ListUnionMemberSr(ModelSerializer):
    class Meta:
        model = UnionMember
        exclude = []
    def to_representation(self, obj):
        rep = super().to_representation(obj)
        user = obj.user
        
        if obj.position is not None:
            rep["position"] = obj.position.name
            
        if obj.gender is not None:
            rep["gender"] = GENDER_DICT.get(obj.gender, "")
        
        rep["full_name"] = obj.full_name
        rep["first_name"] = user.first_name
        rep["last_name"] = user.last_name
        rep["email"] = user.email
        
        if user.phone_number is None:
            rep["phone_number"] = ""
        else:
            rep["phone_number"] = str(user.phone_number)    
        
        rep["organization"] = obj.organization.str if obj.organization else None
        rep["organization_id"] = obj.organization.id if obj.organization else None
        
        return rep

class UnionMemberDetailSr(ModelSerializer):
    class Meta:
        model = UnionMember
        exclude = []

    def to_representation(self, obj):
        rep = super().to_representation(obj)
        user = obj.user
        rep["email"] = user.email
        rep["phone_number"] = str(user.phone_number) if user.phone_number is not None else ""

        rep["gender"] = {
            "id": obj.gender,
            "label": GENDER_DICT.get(obj.gender, "")
        }
        rep["position"] = PositionSr(obj.position).data
        rep["ethnic"] = EthnicSr(obj.ethnic).data
        rep["religion"] = ReligionSr(obj.religion).data
        rep["occupation"] = OccupationSr(obj.occupation).data
        rep["education_level"] = EducationLevelSr(obj.education_level).data
        rep["qualification"] = QualificationSr(obj.qualification).data
        rep["it_level"] = ItLevelSr(obj.it_level).data
        rep["foreign_language_level"] = ForeignLanguageLevelSr(obj.foreign_language_level).data
        rep["political_theory_level"] = PoliticalTheoryLevelSr(obj.political_theory_level).data
        rep["organization"] = {
            "id": obj.organization.id,
            "label": obj.organization.str,
            "parent_ids": obj.organization.parent_ids,
        } if obj.organization else None

        return rep
