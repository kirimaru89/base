class SourceType:
    NEWS = 1
    CAMPAIGN = 2
    CONTEST = 3


SOURCE_TYPE_CHOICES = (
    (SourceType.NEWS, "Tin tức"),
    (SourceType.CAMPAIGN, "Đợt tình nguyện"),
    (SourceType.CONTEST, "Cuộc thi"),
)

SOURCE_TYPE_DIC = dict(SOURCE_TYPE_CHOICES)

SOURCE_TYPES = [{"value": k, "label": v} for k, v in SOURCE_TYPE_CHOICES]
