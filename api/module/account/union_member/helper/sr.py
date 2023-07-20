from rest_framework.serializers import ModelSerializer

from module.account.union_member.consts import GENDER_DICT
from module.account.union_member.models import UnionMember


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


class UnionMemberDetailSr(ModelSerializer):
    class Meta:
        model = UnionMember
        exclude = []

    def to_representation(self, obj):
        rep = super().to_representation(obj)
        user = obj.user
        rep["email"] = user.email
        if user.phone_number is None:
            rep["phone_number"] = ""
        else:
            rep["phone_number"] = str(user.phone_number)    
        rep["gender"] = GENDER_DICT.get(obj.gender, "")
        rep["position"] = obj.position.name if obj.position else ""
        rep["ethnic"] = obj.ethnic.name if obj.ethnic else ""
        rep["religion"] = obj.religion.name if obj.religion else ""
        rep["occupation"] = obj.occupation.name if obj.occupation else ""
        rep["education_level"] = obj.education_level.name if obj.education_level else ""
        rep["qualification"] = obj.qualification.name if obj.qualification else ""
        rep["it_level"] = obj.it_level.name if obj.it_level else ""
        rep["foreign_language_level"] = obj.foreign_language_level.name if obj.foreign_language_level else ""
        rep["political_theory_level"] = obj.political_theory_level.name if obj.political_theory_level else ""
        rep["activities_place"] = obj.activities_place.str if obj.activities_place else ""
        rep["participated_place"] = "Thôn Sơn Phước, Xã Hòa Ninh, Huyện Hoà Vang, Đà Nẵng"
        return rep
