from custom_type import query_obj
from module.account.union_member.helper.sr import UnionMemberSr
from module.account.user.helper.util import UserUtil


class UnionMemberUtil:
    @staticmethod
    def create_union_member(data: dict) -> query_obj:
        data["is_staff"] = False
        user = UserUtil.create_user(data)

        # Create union_member
        union_member_data = data | {"user": user.pk}
        sr = UnionMemberSr(data=union_member_data)
        sr.is_valid(raise_exception=True)
        return sr.save()

    @staticmethod
    def update_union_member(union_member: query_obj, data: dict) -> query_obj:
        user = UserUtil.update_user(union_member.user, data)

        # Update union_member
        union_member_data = data | {"user": user.pk}
        sr = UnionMemberSr(union_member, data=union_member_data, partial=True)
        sr.is_valid(raise_exception=True)
        return sr.save()
