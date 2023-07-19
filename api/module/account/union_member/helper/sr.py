from rest_framework.serializers import ModelSerializer
from module.account.union_member.models import UnionMember


class UnionMemberSr(ModelSerializer):
    class Meta:
        model = UnionMember
        exclude = []

    def to_representation(self, obj):
        rep = super().to_representation(obj)
        user = obj.user
        rep["full_name"] = obj.full_name
        rep["first_name"] = user.first_name
        rep["last_name"] = user.last_name
        rep["email"] = user.email
        rep["phone_number"] = str(user.phone_number)
        return rep
