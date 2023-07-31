class BeneficiaryTypes:
    BCND = 1
    TN = 2
    TNKN = 3
    CCCM = 4


BENEFICIARY_CHOICES = (
    (BeneficiaryTypes.BCND, "Bà con nhân dân"),
    (BeneficiaryTypes.TN, "Thiếu nhi"),
    (BeneficiaryTypes.TNKN, "Thanh niên khởi nghiệp"),
    (BeneficiaryTypes.CCCM, "Gia đình có công với cách mạng"),
)

BENEFICIARY_DIC = dict(BENEFICIARY_CHOICES)

BENEFICIARY_TYPES = [{"value": k, "label": v} for k, v in BENEFICIARY_CHOICES]
