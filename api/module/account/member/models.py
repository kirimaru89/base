from django.db import models
from django.conf import settings

from .consts import (
    ETHNIC_CHOICES,
    Ethnic,
    POLITICAL_THEORY_LEVEL_CHOICES,
    PoliticalTheoryLevel,
    FOREIGN_LANGUAGE_LEVEL_CHOICES,
    ForeignLanguageLevel,
    IT_LEVEL_CHOICES,
    ItLevel,
    QUALIFICATION_CHOICES,
    Qualification,
    EDUCATION_LEVEL_CHOICES,
    EducationLevel,
    RELIGION_CHOICES,
    Religion,
    GENDER_CHOICES,
    Gender,
)

from module.dropdown.organization.models import Organization
from module.dropdown.occupation.models import Occupation
from module.dropdown.position.models import Position

from service.framework.model.timestamped_model import TimeStampedModel


# Create your models here.


class Member(TimeStampedModel):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False
    )

    position = models.ForeignKey(
        Position, on_delete=models.CASCADE, null=True, blank=True, default=None
    )
    occupation = models.ForeignKey(
        Occupation, on_delete=models.CASCADE, null=True, blank=True, default=None
    )
    organization = models.ForeignKey(
        Organization, on_delete=models.CASCADE, null=True, blank=True, default=None
    )
    ethnic = models.IntegerField(
        choices=ETHNIC_CHOICES, default=Ethnic.E1, null=True, blank=True
    )
    religion = models.IntegerField(
        choices=RELIGION_CHOICES, default=Religion.K, null=True, blank=True
    )
    education_level = models.IntegerField(
        choices=EDUCATION_LEVEL_CHOICES,
        default=EducationLevel.TH,
        null=True,
        blank=True,
    )
    qualification = models.IntegerField(
        choices=QUALIFICATION_CHOICES, default=Qualification.SC, null=True, blank=True
    )
    it_level = models.IntegerField(
        choices=IT_LEVEL_CHOICES, default=ItLevel.BASIC, null=True, blank=True
    )
    foreign_language_level = models.IntegerField(
        choices=FOREIGN_LANGUAGE_LEVEL_CHOICES,
        default=ForeignLanguageLevel.LV1,
        null=True,
        blank=True,
    )
    political_theory_level = models.IntegerField(
        choices=POLITICAL_THEORY_LEVEL_CHOICES,
        default=PoliticalTheoryLevel.SC,
        null=True,
        blank=True,
    )

    dob = models.DateField(null=True, blank=True, default=None)
    place_of_origin = models.CharField(
        max_length=255, null=True, blank=True, default=""
    )
    place_of_residence = models.CharField(
        max_length=255, null=True, blank=True, default=""
    )

    full_name = models.CharField(max_length=255, null=False, default="")
    joined_date = models.DateField(null=True, blank=True, default=None)
    gender = models.IntegerField(
        choices=GENDER_CHOICES, default=Gender.FEMALE, null=True, blank=True
    )
    id_number = models.CharField(max_length=255, null=True, blank=True, default="")
    id_issued_date = models.DateField(null=True, blank=True, default=None)
    id_issued_place = models.CharField(
        max_length=255, null=True, blank=True, default=""
    )

    def __str__(self):
        return self.user.email

    @property
    def email(self) -> str:
        return self.user.email

    @property
    def mobile(self) -> str:
        return self.user.mobile

    class Meta:
        db_table = "members"
        ordering = ["-user"]
