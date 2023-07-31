from django.contrib import admin
from .models import Message


class MessageAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "member",
        "source_type",
        "source_id",
        "read_at",
        "created_at",
        "updated_at",
    )
    list_filter = ("source_type",)
    search_fields = (
        "id",
        "title",
        "source_id",
        "member__user__email",
        "member__user__mobile",
    )


admin.site.register(Message, MessageAdmin)
