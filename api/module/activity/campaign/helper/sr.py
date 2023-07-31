from rest_framework.serializers import ModelSerializer
from ..models import Campaign
from module.activity.campaign.consts import CAMPAIGN_TYPES
from module.activity.campaign_attachment.models import CampaignAttachment
from module.activity.campaign_attachment.helper.sr import CampaignAttachmentSr
from module.activity.campaign.consts import CAMPAIGN_STATUSES


class CampaignSr(ModelSerializer):
    class Meta:
        model = Campaign
        exclude = ()
        read_only_fields = ("id",)

class CampaignListSr(ModelSerializer):
    class Meta:
        model = Campaign
        exclude = ()
        read_only_fields = ("id",)
    
    def to_representation(self, obj):
        rep = super().to_representation(obj)
        
        rep["content"] = ""
        
        rep["type_obj"] = next((x for x in CAMPAIGN_TYPES if x["value"] == obj.type), None)
        
        rep["status_obj"] = next((x for x in CAMPAIGN_STATUSES if x["value"] == obj.status), None)
        
        rep["created_by_obj"] = {
            "value": obj.created_by.id,
            "label": obj.created_by.full_name,
        }
        
        attachments = CampaignAttachment.objects.filter(campaign_id=obj.id)
        rep["attachments"] = CampaignAttachmentSr(attachments, many=True).data
        
        return rep
    
class CampaignDetailSr(ModelSerializer):
    class Meta:
        model = Campaign
        exclude = ()
        read_only_fields = ("id",)
    
    def to_representation(self, obj):
        rep = super().to_representation(obj)
        
        rep["type_obj"] = next((x for x in CAMPAIGN_TYPES if x["value"] == obj.type), None)
        
        images = CampaignAttachment.objects.filter(campaign_id=obj.id,type=1)
        imagesData = CampaignAttachmentSr(images, many=True)        
        files = CampaignAttachment.objects.filter(campaign_id=obj.id,type=2)
        filesData = CampaignAttachmentSr(files, many=True)
        
        rep["images"] = imagesData.data
        rep["files"] = filesData.data
        
        rep["status_obj"] = next((x for x in CAMPAIGN_STATUSES if x["value"] == obj.status), None)
        
        rep["created_by_obj"] = {
            "value": obj.created_by.id,
            "label": obj.created_by.full_name,
        }
        
        return rep