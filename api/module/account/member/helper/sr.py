from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework.serializers import (
    ModelSerializer,
    Serializer,
)

from module.dropdown.helper.util import DropdownUtil
from service.validator_service import ValidatorService
from module.account.member.consts import (
    EDUCATION_LEVELS,
    FOREIGN_LANGUAGE_LEVELS,
    GENDERS,
    IT_LEVELS,
    POLITICAL_THEORY_LEVELS,
    QUALIFICATIONS,
    RELIGIONS,
    ETHNICS,
    GENDER_DICT,
    ETHNIC_DIC,
    RELIGION_DIC,
    EDUCATION_LEVEL_DIC,
    QUALIFICATION_DIC,
    IT_LEVEL_DIC,
    POLITICAL_THEORY_LEVEL_DIC,
    FOREIGN_LANGUAGE_LEVEL_DIC,
)
from module.dropdown.organization.models import Organization
from module.dropdown.occupation.models import Occupation
from module.dropdown.position.models import Position
from ..models import Member


name_error_messages = {
    "blank": _("Please enter your name"),
    "max_length": _("Email length can not excess 100 characters"),
}

email_error_messages = {
    "invalid": _("Invalid email format"),
    "blank": _("Please enter your password"),
    "max_length": _("Email length can not excess 100 characters"),
}

mobile_error_messages = {
    "blank": _("Mobile can not be blank"),
    "max_length": _("Mobile length can not excess 50 characters"),
}


class RegistrationSr(Serializer):
    full_name = serializers.CharField(
        max_length=100, error_messages=name_error_messages
    )
    email = serializers.EmailField(max_length=100, error_messages=email_error_messages)
    mobile = serializers.CharField(
        max_length=50,
        validators=[ValidatorService.mobile_validator],
        error_messages=mobile_error_messages,
    )
    password = serializers.CharField(
        validators=[ValidatorService.password_validator],
    )


class MemberSr(ModelSerializer):
    class Meta:
        model = Member
        exclude = []

    def to_representation(self, obj):
        rep = super().to_representation(obj)
        user = obj.user
        rep["full_name"] = obj.full_name
        rep["first_name"] = user.first_name
        rep["last_name"] = user.last_name
        rep["email"] = user.email
        rep["mobile"] = str(user.mobile)
        rep["member"] = str(user.member)
        rep["groups"] = user.groups.values_list("id", flat=True)
        rep["is_active"] = obj.user.is_active
        return rep


class MemberListSr(ModelSerializer):
    class Meta:
        model = Member
        exclude = []

    def to_representation(self, obj):
        rep = super().to_representation(obj)
        user = obj.user

        if obj.position is not None:
            rep["position"] = obj.position.title

        if obj.gender is not None:
            rep["gender"] = GENDER_DICT.get(obj.gender, "")

        rep["email"] = user.email

        rep["mobile"] = "" if user.mobile is None else str(user.mobile)
        rep["organization"] = obj.organization.str if obj.organization else None

        return rep


class MemberDetailSr(ModelSerializer):
    class Meta:
        model = Member
        exclude = []

    def to_representation(self, obj):
        rep = super().to_representation(obj)
        user = obj.user

        rep["email"] = user.email
        rep["mobile"] = str(user.mobile) if user.mobile is not None else ""

        position_obj = (
            Position.objects.filter(pk=obj.position.id).first()
            if obj.position is not None
            else None
        )
        if position_obj is not None:
            rep["position_obj"] = {
                "value": position_obj.id,
                "label": position_obj.title,
            }
        else:
            rep["position_obj"] = None

        occupation_obj = (
            Occupation.objects.filter(pk=obj.occupation.id).first()
            if obj.occupation is not None
            else None
        )
        if occupation_obj is not None:
            rep["occupation_obj"] = {
                "value": occupation_obj.id,
                "label": occupation_obj.title,
            }
        else:
            rep["occupation_obj"] = None

        organization_obj = (
            Organization.objects.filter(pk=obj.organization.id).first()
            if obj.organization is not None
            else None
        )
        if organization_obj is not None:
            rep["organization_obj"] = {
                "value": organization_obj.id,
                "label": organization_obj.str,
            }
        else:
            rep["organization_obj"] = None

        rep["ethnic_obj"] = next((x for x in ETHNICS if x["value"] == obj.ethnic), None)
        rep["religion_obj"] = next(
            (x for x in RELIGIONS if x["value"] == obj.religion), None
        )
        rep["education_level_obj"] = next(
            (x for x in EDUCATION_LEVELS if x["value"] == obj.education_level), None
        )
        rep["qualification_obj"] = next(
            (x for x in QUALIFICATIONS if x["value"] == obj.qualification), None
        )
        rep["it_level_obj"] = next(
            (x for x in IT_LEVELS if x["value"] == obj.it_level), None
        )
        rep["foreign_language_level_obj"] = next(
            (
                x
                for x in FOREIGN_LANGUAGE_LEVELS
                if x["value"] == obj.foreign_language_level
            ),
            None,
        )
        rep["political_theory_level_obj"] = next(
            (
                x
                for x in POLITICAL_THEORY_LEVELS
                if x["value"] == obj.political_theory_level
            ),
            None,
        )
        rep["gender_obj"] = next((x for x in GENDERS if x["value"] == obj.gender), None)

        return rep


class MemberProfileSr(ModelSerializer):
    class Meta:
        model = Member
        exclude = []

    def to_representation(self, obj):
        is_update = self.context.get("is_update", False)
        rep = super().to_representation(obj)
        
        user = obj.user
        
        rep["email"] = user.email
        rep["mobile"] = str(user.mobile) if user.mobile is not None else ""
        
        position_obj = (
            Position.objects.filter(pk=obj.position.id).first()
            if obj.position is not None
            else None
        )
        if position_obj is not None:
            rep["position_obj"] = {
                "value": position_obj.id,
                "label": position_obj.title,
            }
        else:
            rep["position_obj"] = None

        occupation_obj = (
            Occupation.objects.filter(pk=obj.occupation.id).first()
            if obj.occupation is not None
            else None
        )
        if occupation_obj is not None:
            rep["occupation_obj"] = {
                "value": occupation_obj.id,
                "label": occupation_obj.title,
            }
        else:
            rep["occupation_obj"] = None

        organization_obj = (
            Organization.objects.filter(pk=obj.organization.id).first()
            if obj.organization is not None
            else None
        )
        if organization_obj is not None:
            rep["organization_obj"] = {
                "value": organization_obj.id,
                "label": organization_obj.str,
            }
        else:
            rep["organization_obj"] = None

        rep["ethnic_obj"] = next((x for x in ETHNICS if x["value"] == obj.ethnic), None)
        rep["religion_obj"] = next(
            (x for x in RELIGIONS if x["value"] == obj.religion), None
        )
        rep["education_level_obj"] = next(
            (x for x in EDUCATION_LEVELS if x["value"] == obj.education_level), None
        )
        rep["qualification_obj"] = next(
            (x for x in QUALIFICATIONS if x["value"] == obj.qualification), None
        )
        rep["it_level_obj"] = next(
            (x for x in IT_LEVELS if x["value"] == obj.it_level), None
        )
        rep["foreign_language_level_obj"] = next(
            (
                x
                for x in FOREIGN_LANGUAGE_LEVELS
                if x["value"] == obj.foreign_language_level
            ),
            None,
        )
        rep["political_theory_level_obj"] = next(
            (
                x
                for x in POLITICAL_THEORY_LEVELS
                if x["value"] == obj.political_theory_level
            ),
            None,
        )
        rep["gender_obj"] = next((x for x in GENDERS if x["value"] == obj.gender), None)

        if is_update:
            return rep

        return {"data": rep, "extra": {"options": DropdownUtil.get_member_options()}}
