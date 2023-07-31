from django.contrib import admin
from rangefilter.filter import DateRangeFilter

from .models import Campaign
from ...article.category.helper.admin_filter import CreatedByFilter, UpdatedByFilter


class CampaignAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "type",
        "status",
        "registration_from",
        "registration_to",
        "created_by",
        "updated_by",
    )
    readonly_fields = (
        "created_at",
        "updated_at",
    )
    list_filter = (
        "type",
        CreatedByFilter,
        UpdatedByFilter,
        ("registration_from", DateRangeFilter),
        ("registration_to", DateRangeFilter),
        ("created_at", DateRangeFilter),
        ("updated_at", DateRangeFilter),
    )
    search_fields = ("id", "title", "place")


admin.site.register(Campaign, CampaignAdmin)
