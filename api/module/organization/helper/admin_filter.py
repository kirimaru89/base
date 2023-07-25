
from module.organization.models import Organization
from service.input_filter import InputFilter


class ParentIdFilter(InputFilter):
    parameter_name = "parent_id"
    title = "Parent Id"

    def queryset(self, request, queryset):
        try:
            return (
                Organization.objects.filter(parent__id=self.value())
                if self.value() is not None
                else queryset.all()
            )
        except ValueError:
            return queryset.all()
