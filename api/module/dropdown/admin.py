from django.contrib import admin

from .education_level.models import EducationLevel
from .ethnic.models import Ethnic
from .foreign_language_level.models import ForeignLanguageLevel
from .it_level.models import ItLevel
from .occupation.models import Occupation
from .political_theory_level.models import PoliticalTheoryLevel
from .position.models import Position
from .qualification.models import Qualification
from .religion.models import Religion

admin.site.register(Position)
admin.site.register(Ethnic)
admin.site.register(Religion)
admin.site.register(Occupation)
admin.site.register(EducationLevel)
admin.site.register(Qualification)
admin.site.register(ItLevel)
admin.site.register(ForeignLanguageLevel)
admin.site.register(PoliticalTheoryLevel)
