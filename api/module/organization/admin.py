from django.contrib import admin

from module.organization.helper.admin_filter import ParentIdFilter
from module.organization.models import Organization


class OrganizationAdmin(admin.ModelAdmin):
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


admin.site.register(Organization, OrganizationAdmin)
