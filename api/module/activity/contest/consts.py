class ContestStatus:
    NOT_STARTED = 1
    STARTED = 2
    FINISHED = 3


CONTEST_STATUS_CHOICES = (
    (ContestStatus.NOT_STARTED, "Chưa bắt đầu"),
    (ContestStatus.STARTED, "Đang diễn ra"),
    (ContestStatus.FINISHED, "Đã kết thúc"),
)

CONTEST_STATUS_DICT = dict(CONTEST_STATUS_CHOICES)
