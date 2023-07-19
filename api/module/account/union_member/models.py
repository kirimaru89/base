from django.db import models
from django.conf import settings

from module.account.union_member.consts import GENDER_CHOICES
from module.dropdown.education_level.models import EducationLevel
from module.dropdown.ethnic.models import Ethnic
from module.dropdown.foreign_language_level.models import ForeignLanguageLevel
from module.dropdown.it_level.models import ItLevel
from module.dropdown.occupation.models import Occupation
from module.dropdown.political_theory_level.models import PoliticalTheoryLevel
from module.dropdown.position.models import Position
from module.dropdown.qualification.models import Qualification
from module.dropdown.religion.models import Religion
from service.framework.model.timestamped_model import TimeStampedModel


class UnionMember(TimeStampedModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    joined_date = models.DateField(null=True, blank=True)
    gender = models.IntegerField(choices=GENDER_CHOICES, null=True)
    identity_number = models.CharField(max_length=255)
    participated_place_id = models.IntegerField()
    issued_date = models.DateField(null=True, blank=True)
    issued_place = models.CharField(max_length=255)
    position = models.ForeignKey(
        Position, related_name="union_members", on_delete=models.SET_NULL, null=True, blank=True, default=None,
    )
    ethnic = models.ForeignKey(
        Ethnic, related_name="union_members", on_delete=models.SET_NULL, null=True, blank=True, default=None,
    )
    religion = models.ForeignKey(
        Religion, related_name="union_members", on_delete=models.SET_NULL, null=True, blank=True, default=None,
    )
    occupation = models.ForeignKey(
        Occupation, related_name="union_members", on_delete=models.SET_NULL, null=True, blank=True, default=None,
    )
    education_level = models.ForeignKey(
        EducationLevel, related_name="union_members", on_delete=models.SET_NULL, null=True, blank=True, default=None,
    )
    qualification = models.ForeignKey(
        Qualification, related_name="union_members", on_delete=models.SET_NULL, null=True, blank=True, default=None,
    )
    it_level = models.ForeignKey(
        ItLevel, related_name="union_members", on_delete=models.SET_NULL, null=True, blank=True, default=None,
    )
    foreign_language_level = models.ForeignKey(
        ForeignLanguageLevel, related_name="union_members", on_delete=models.SET_NULL, null=True, blank=True, default=None,
    )
    political_theory_level = models.ForeignKey(
        PoliticalTheoryLevel, related_name="union_members", on_delete=models.SET_NULL, null=True, blank=True, default=None,
    )

    def __str__(self):
        return f"UnionMember #{self.id} - {self.full_name}"

    @property
    def full_name(self) -> str:
        return self.user.full_name

    @property
    def email(self) -> str:
        return self.user.email

    @property
    def phone_number(self) -> str:
        return self.user.phone_number

    def delete(self, *args, **kwargs):
        self.user.delete()
        return super().delete(*args, **kwargs)

    class Meta:
        db_table = "union_members"
        ordering = ["-user"]
