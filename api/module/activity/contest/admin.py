from django.contrib import admin
from .models import Contest


class ContestAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "questions",
        "uid",
        "title",
        "duration",
        "min_score",
        "start_at",
        "end_at",
    )

    def questions(self, obj):
        return obj.questions.count()


admin.site.register(Contest, ContestAdmin)
