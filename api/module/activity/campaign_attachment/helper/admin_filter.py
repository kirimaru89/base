from service.framework.admin.input_filter import InputFilter


class CampaignFilter(InputFilter):
    parameter_name = "campaign_id"
    title = "Campaign Id"

    def queryset(self, request, queryset):
        if self.value() is not None:
            campaign_id = self.value()
            return queryset.filter(campaign=campaign_id)
        return queryset.all()
