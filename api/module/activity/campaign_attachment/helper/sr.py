from rest_framework.serializers import ModelSerializer
from ..models import CampaignAttachment
from ..consts import CAMPAIGN_ATTACHMENT_TYPES


class CampaignAttachmentSr(ModelSerializer):
    class Meta:
        model = CampaignAttachment
        exclude = ()
        read_only_fields = ("id",)
        
    def to_representation(self, obj):
        rep = super().to_representation(obj)        
        rep["type_obj"] = next((x for x in CAMPAIGN_ATTACHMENT_TYPES if x["value"] == obj.type), None)        
        return rep