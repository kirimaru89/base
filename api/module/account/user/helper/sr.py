from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework.validators import UniqueValidator
from service.format_service import FormatService
from service.validator_service import ValidatorService

User = get_user_model()


name_error_messages = {
    "blank": _("Please enter your name"),
    "max_length": _("Email length can not excess 100 characters"),
}

email_error_messages = {
    "invalid": _("Invalid email format"),
    "blank": _("Please enter your password"),
    "max_length": _("Email length can not excess 100 characters"),
}

phone_number_error_messages = {
    "blank": _("Phone number can not be blank"),
    "max_length": _("Phone number length can not excess 50 characters"),
}


class SignupSr(Serializer):
    name = serializers.CharField(max_length=100, error_messages=name_error_messages)
    email = serializers.EmailField(max_length=100, error_messages=email_error_messages)
    phone_number = serializers.CharField(
        max_length=50,
        validators=[ValidatorService.phone_number_validator],
        error_messages=phone_number_error_messages,
    )
    password = serializers.CharField(
        validators=[ValidatorService.password_validator],
    )


class UserSr(ModelSerializer):
    class Meta:
        model = User
        exclude = []

    email = serializers.CharField(
        validators=[
            UniqueValidator(queryset=User.objects.all(), message="Duplicate email")
        ]
    )

    def to_internal_value(self, data):
        if "phone_number" in data:
            phone_number = data.get("phone_number")
            phone_number = FormatService.phone_to_canonical_format(phone_number)
            if not phone_number:
                phone_number = None
            data["phone_number"] = phone_number

        if "email" in data:
            email = data.get("email").lower()
            data["username"] = email
            data["email"] = email

        if "password" in data:
            data["password"] = make_password(data.get("password"))

        return super().to_internal_value(data)

    def to_representation(self, obj):
        return {
            "id": obj.pk,
            "full_name": obj.full_name,
            "is_active": obj.is_active,
            "is_staff": obj.is_staff,
        }
