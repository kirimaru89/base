class CampaignType:
    HM = 1
    GDNG = 2
    GD = 3
    TC = 4


CAMPAIGN_TYPE_CHOICES = (
    (CampaignType.HM, "Hiến máu"),
    (CampaignType.GDNG, "Giúp đỡ người già"),
    (CampaignType.GD, "Giảng dạy"),
    (CampaignType.TC, "Trồng cây"),
)

CAMPAIGN_TYPE_DIC = dict(CAMPAIGN_TYPE_CHOICES)

CAMPAIGN_TYPES = [{"value": k, "label": v} for k, v in CAMPAIGN_TYPE_CHOICES]


class BeneficiaryType:
    BCND = 1
    TN = 2
    TNKN = 3
    CCCM = 4


BENEFICIARY_TYPE_CHOICES = (
    (BeneficiaryType.BCND, "Bà con nhân dân"),
    (BeneficiaryType.TN, "Thiếu nhi"),
    (BeneficiaryType.TNKN, "Thanh niên khởi nghiệp"),
    (BeneficiaryType.CCCM, "Gia đình có công với cách mạng"),
)

BENEFICIARY_TYPE_DIC = dict(BENEFICIARY_TYPE_CHOICES)

BENEFICIARY_TYPES = [{"value": k, "label": v} for k, v in BENEFICIARY_TYPE_CHOICES]

class CampaignStatus:
    ON_GOING = 1
    SOON = 2
    ENDED = 3


CAMPAIGN_STATUS_CHOICES = (
    (CampaignStatus.ON_GOING, "Đang diễn ra"),
    (CampaignStatus.SOON, "Sắp diễn ra"),
    (CampaignStatus.ENDED, "Đã kết thúc"),
)

CAMPAIGN_STATUS_DIC = dict(CAMPAIGN_STATUS_CHOICES)

CAMPAIGN_STATUSES = [{"value": k, "label": v} for k, v in CAMPAIGN_STATUS_CHOICES]