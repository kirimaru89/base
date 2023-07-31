from django.contrib import admin
from module.activity.exam_question.models import ExamQuestion
from .models import Exam


class ExamQuestionInline(admin.TabularInline):
    model = ExamQuestion
    readonly_fields = ("id",)
    extra = 0


class ExamAdmin(admin.ModelAdmin):
    inlines = [ExamQuestionInline]
    list_display = (
        "id",
        "questions",
        "member",
        "contest",
        "score",
        "submitted_at",
        "started_at",
        "finished_at",
    )

    def questions(self, obj):
        return obj.exam_questions.count()


admin.site.register(Exam, ExamAdmin)
