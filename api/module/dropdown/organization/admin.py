from django.contrib import admin
from rangefilter.filter import DateRangeFilter

from module.dropdown.organization.models import Organization


class OrganizationAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "type",
        "level",
        "parent",
        "root_parent",
        "rep_email",
        "rep_mobile",
        "rep_name",
    )
    readonly_fields = (
        "created_at",
        "updated_at",
    )
    list_filter = (
        "type",
        "level",
        ("created_at", DateRangeFilter),
        ("updated_at", DateRangeFilter),
    )
    search_fields = ("id", "title", "rep_name")


admin.site.register(Organization, OrganizationAdmin)
