from service.framework.admin.input_filter import InputFilter


class CreatedByFilter(InputFilter):
    parameter_name = "created_by"
    title = "Created By"

    def queryset(self, request, queryset):
        if self.value() is not None:
            created_by = self.value()
            return queryset.filter(created_by=created_by)
        return queryset.all()


class UpdatedByFilter(InputFilter):
    parameter_name = "updated_by"
    title = "Updated By"

    def queryset(self, request, queryset):
        if self.value() is not None:
            updated_by = self.value()
            return queryset.filter(updated_by=updated_by)
        return queryset.all()
