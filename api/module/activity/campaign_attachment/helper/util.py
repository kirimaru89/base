from module.activity.campaign_attachment.helper.sr import CampaignAttachmentSr
from module.activity.campaign_attachment.models import CampaignAttachment


class CampaignAttachmentUtil:
    @staticmethod
    def get_specific_attachments(payload, attachment_ids):
        new_attachments = list(filter(lambda d: 'id' not in d, payload))
        payload_ids = [d.get('id') for d in payload if 'id' in d]
        del_ids = set(attachment_ids) - set(payload_ids)
        return del_ids, new_attachments

    @staticmethod
    def update_attachment(payload, campaign):
        att_ids = campaign.campaign_attachments.all().values_list("id", flat=True)
        del_ids, new_items = CampaignAttachmentUtil.get_specific_attachments(payload, att_ids)
        CampaignAttachmentUtil.delete_attachments(del_ids)
        serializer = CampaignAttachmentSr(data=new_items, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

    @staticmethod
    def delete_attachments(ids):
        try:
            for id in ids:
                CampaignAttachment.objects.get(pk=id).delete()
        except Exception as e:
            print(repr(e))
