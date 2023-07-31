from django.contrib import admin
from rangefilter.filter import DateRangeFilter

from module.activity.campaign_attachment.helper.admin_filter import CampaignFilter
from module.activity.campaign_attachment.models import CampaignAttachment


class CampaignAttachmentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "type",
        "campaign",
        "created_at",
        "updated_at",
    )
    readonly_fields = (
        "created_at",
        "updated_at",
    )
    list_filter = (
        "type",
        CampaignFilter,
        ("created_at", DateRangeFilter),
        ("updated_at", DateRangeFilter),
    )
    search_fields = ("id", "title")


admin.site.register(CampaignAttachment, CampaignAttachmentAdmin)
