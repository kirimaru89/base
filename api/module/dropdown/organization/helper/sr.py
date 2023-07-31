from rest_framework.serializers import ModelSerializer, SerializerMethodField
from module.dropdown.organization.models import Organization
from module.dropdown.organization.consts import (
    ORGANIZATION_TYPE_DICT,
    ORGANIZATION_LEVEL_DICT,
)


class OrganizationSr(ModelSerializer):
    class Meta:
        model = Organization
        exclude = ()
        read_only_fields = ("id",)

    def to_representation(self, obj):
        rep = super().to_representation(obj)
        rep["type_obj"] = {
            "value": obj.type,
            "label": ORGANIZATION_TYPE_DICT.get(obj.type, ""),
        }
        rep["level_obj"] = {
            "value": obj.level,
            "label": ORGANIZATION_LEVEL_DICT.get(obj.level, ""),
        }
        rep["parent_obj"] = {
            "value": obj.parent_id,
            "label": obj.parent.title if obj.parent else "",
        }
        return rep


class OrganizationTreeSr(ModelSerializer):
    class Meta(Organization.Meta):
        model = Organization
        fields = ("id", "key", "title", "isLeaf", "children")

    key = SerializerMethodField()
    title = SerializerMethodField()
    isLeaf = SerializerMethodField()
    children = SerializerMethodField()

    def get_key(self, obj):
        return str(obj.pk)

    def get_title(self, obj):
        return obj.title

    def get_isLeaf(self, obj):
        return len(Organization.objects.get_childs(obj)) == 0

    def get_children(self, obj):
        queryset = obj.children.all().order_by("title")
        return OrganizationTreeSr(queryset, many=True).data
