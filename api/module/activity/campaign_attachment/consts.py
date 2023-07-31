class CampaignAttachmentType:
    IMAGE = 1
    FILE = 2


CAMPAIGN_ATTACHMENT_TYPE_CHOICES = (
    (CampaignAttachmentType.IMAGE, "Ảnh"),
    (CampaignAttachmentType.FILE, "Tệp tài liệu"),
)

CAMPAIGN_ATTACHMENT_TYPE_DIC = dict(CAMPAIGN_ATTACHMENT_TYPE_CHOICES)

CAMPAIGN_ATTACHMENT_TYPES = [
    {"value": k, "label": v} for k, v in CAMPAIGN_ATTACHMENT_TYPE_CHOICES
]
