from django.contrib.auth.models import Group, Permission
from custom_type import query_set, query_obj
from module.account.helper.sr import GroupSr
from module.account.member.models import Member
from module.account.member.helper.sr import MemberSr
from module.account.user.helper.util import UserUtil


class MemberUtil:
    @staticmethod
    def seeding(index: int, single: bool = False, save: bool = True) -> query_set:
        # sourcery skip: raise-specific-error

        if index == 0:
            raise Exception("Indext must be start with 1.")

        def get_data(i: int) -> dict:
            mobile = f"+849066965{i}" if i >= 10 else f"+8490669652{i}"
            test_password = UserUtil.get_default_test_pwd()
            data = {
                "email": f"test{i}@gmail.com",
                "mobile": mobile,
                "first_name": f"first{i}",
                "last_name": f"last{i}",
                "password": test_password,
            }

            if not save:
                return data

            try:
                instance = Member.objects.get(user__username=data["email"])
            except Member.DoesNotExist:
                instance = MemberUtil.create_member(data)
                group, _ = Group.objects.get_or_create(name="test")
                group.permissions.set(Permission.objects.all())
                instance.user.groups.set([group])

            return instance

        def get_list_data(index):
            return [get_data(i) for i in range(1, index + 1)]

        return get_data(index) if single else get_list_data(index)

    @staticmethod
    def create_member(data: dict) -> query_obj:
        user = UserUtil.create_user(data)

        # Create member
        member_data = data | {"user": user.pk}
        sr = MemberSr(data=member_data)
        sr.is_valid(raise_exception=True)
        member = sr.save()
        member_group, _ = Group.objects.get_or_create(name="Member")
        member.user.groups.add(member_group)
        return member

    @staticmethod
    def update_member(member: query_obj, data: dict) -> query_obj:
        user = UserUtil.update_user(member.user, data)

        # Update member
        member_data = data | {"user": user.pk}
        sr = MemberSr(member, data=member_data, partial=True)
        sr.is_valid(raise_exception=True)
        return sr.save()

    @staticmethod
    def get_list_group() -> list:
        raw_data = GroupSr(Group.objects.exclude(name="customer"), many=True).data
        return [{"value": group["id"], "label": group["name"]} for group in raw_data]
