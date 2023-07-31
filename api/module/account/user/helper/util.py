from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.hashers import make_password, check_password
from django.template.loader import render_to_string
from custom_type import query_obj
from service.email_service import EmailService
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
            data["password"] = StringService.get_random_digits(12)
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

    @staticmethod
    def send_new_password_email(to_email, password, lang):
        subject = (
            "[Thanh niên Đà Nẵng] Thông báo cấp lại mật khẩu mới"
            if lang == "vi-vn"
            else "[Da Nang youth] Reset new password"
        )
        body = render_to_string(
            f"emails/forgot_password/{lang}.html",
            {
                "password": password,
            },
        )
        EmailService.send_email_async(subject, body, to_email)

    @staticmethod
    def forgot_password(email, lang="vi-vn"):
        try:
            user = UserUtil.get_user_by_username(email)
            if not user:
                return False
            password = StringService.get_random_digits(12)
            user.password = make_password(password)
            user.save()
            UserUtil.send_new_password_email(email, password, lang)
            return True
        except Exception as e:
            print(repr(e))
            return False
