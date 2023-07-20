from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _
from custom_type import query_obj
from service.string_service import StringService
from .sr import UserSr

User = get_user_model()


class UserUtil:
    @staticmethod
    def get_default_test_pwd():
        return "SamplePassword123!@#"

    @staticmethod
    def create_user(data: dict) -> query_obj:
        if not data.get("password"):
            data["password"] = "SamplePassword123!@#" #StringService.get_random_digits(12)
        sr = UserSr(data=data)
        sr.is_valid(raise_exception=True)
        user = sr.save()

        if "groups" in data:
            groups = [int(group) for group in data.get("groups", [])]
            if list(groups):
                group_list = Group.objects.filter(id__in=groups)
                for group in group_list:
                    group.user_set.add(user)
        return user

    @staticmethod
    def update_user(user: query_obj, data: dict) -> query_obj:
        user = user
        sr = UserSr(user, data=data, partial=True)
        sr.is_valid(raise_exception=True)
        user = sr.save()

        if "groups" in data:
            groups = [int(group) for group in data.get("groups", [])]
            for group in user.groups.all():
                group.user_set.remove(user)

            if list(groups):
                group_list = Group.objects.filter(id__in=groups)
                for group in group_list:
                    group.user_set.add(user)
        return user

    @staticmethod
    def get_user_by_username(username: str) -> query_obj:
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            return None

    @staticmethod
    def is_duplicate_username(username):
        message = _(
            'This email already exists in the system. Please, use another email to register or use the "Forgot password" function.'
        )
        user = UserUtil.get_user_by_username(username)
        if user:
            return {"detail": message}
        return False
