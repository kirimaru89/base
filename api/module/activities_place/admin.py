from django.contrib import admin

from module.activities_place.helper.admin_filter import ParentIdFilter
from module.activities_place.models import ActivitiesPlace


class ActivitiesPlaceAdmin(admin.ModelAdmin):
    readonly_fields = (
        "created_at",
        "updated_at",
    )
    list_display = (
        "id",
        "name",
        "parent",
        "type",
        "level",
        "email",
        "phone_number",
        "representative",
    )
    list_filter = (
        ParentIdFilter,
        "type",
        "level",
    )
    search_fields = ("id", "title", "representative")


admin.site.register(ActivitiesPlace, ActivitiesPlaceAdmin)
