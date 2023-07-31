class NewsType:
    NORMAL = 1
    FEATURED = 2


NEWS_TYPE_CHOICES = (
    (NewsType.NORMAL, "Tin thường"),
    (NewsType.FEATURED, "Tin nổi bật"),
)

NEWS_TYPE_DIC = dict(NEWS_TYPE_CHOICES)

NEWS_TYPES = [{"value": k, "label": v} for k, v in NEWS_TYPE_CHOICES]


class NewsStatus:
    INACTIVE = 1
    ACTIVE = 2


NEWS_STATUS_CHOICES = (
    (NewsStatus.INACTIVE, "Không hiệu lực"),
    (NewsStatus.ACTIVE, "Hiệu lực"),
)

NEWS_STATUS_DIC = dict(NEWS_STATUS_CHOICES)

NEWS_STATUSS = [{"value": k, "label": v} for k, v in NEWS_STATUS_CHOICES]
