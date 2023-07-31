from django.contrib import admin

from module.noti.device.models import DeviceToken


class DeviceTokenAdmin(admin.ModelAdmin):
    list_display = ("id", "member", "type", "active")
    list_filter = ("type", "active")
    search_fields = ("id", "member__user__email", "member__user__mobile",)


admin.site.register(DeviceToken, DeviceTokenAdmin)
