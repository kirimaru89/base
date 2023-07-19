from django.contrib import admin
# from rangefilter.filter import DateRangeFilter

from module.account.union_member.models import UnionMember


class UnionMemberAdmin(admin.ModelAdmin):
    raw_id_fields = ("user",)
    readonly_fields = (
        "created_at",
        "updated_at",
    )
    list_display = (
        "__str__",
        "joined_date",
        "gender",
        "identity_number",
    )
    list_filter = (
        # ("created_at", DateRangeFilter),
        # ("updated_at", DateRangeFilter),
    )
    search_fields = ("id", "user__email", "user__username")


admin.site.register(UnionMember, UnionMemberAdmin)
