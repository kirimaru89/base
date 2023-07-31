class OrganizationType:
    DNNN = 1
    DNNNN = 2
    CNVC = 3
    LLVT = 4
    TH = 5
    DT = 6
    NT = 7
    CQDN = 8


ORGANIZATION_TYPE_CHOICES = (
    (OrganizationType.DNNN, "Khối doanh nghiệp nhà nước"),
    (OrganizationType.DNNNN, "Khối doanh nghiệp ngoài nhà nước"),
    (OrganizationType.CNVC, "Khối công chức, viên chức"),
    (OrganizationType.LLVT, "Khối lực lượng, vũ trang"),
    (OrganizationType.TH, "Khối trường học"),
    (OrganizationType.DT, "Khối đô thị"),
    (OrganizationType.NT, "Khối nông thôn"),
    (OrganizationType.CQDN, "Khối cơ quan và doanh nghiệp"),
)

ORGANIZATION_TYPE_DICT = dict(ORGANIZATION_TYPE_CHOICES)

ORGANIZATION_TYPES = [{"value": k, "label": v} for k, v in ORGANIZATION_TYPE_CHOICES]


class OrganizationLevel:
    CITY = 1
    DISTRICT = 2
    UPPER_CHAPTER = 3
    CHAPTER = 4
    GRASS_ROOT = 5


ORGANIZATION_LEVEL_CHOICES = (
    (OrganizationLevel.CITY, "Thành phố"),
    (OrganizationLevel.DISTRICT, "Quận (và tương đương)"),
    (OrganizationLevel.UPPER_CHAPTER, "Đoàn giao quyền cấp trên cơ sở"),
    (OrganizationLevel.CHAPTER, "Đoàn cơ sở / Chi Đoàn cơ sở / Liên chi Đoàn"),
    (OrganizationLevel.GRASS_ROOT, "Chi Đoàn"),
)

ORGANIZATION_LEVEL_DICT = dict(ORGANIZATION_LEVEL_CHOICES)

ORGANIZATION_LEVELS = [{"value": k, "label": v} for k, v in ORGANIZATION_LEVEL_CHOICES]
