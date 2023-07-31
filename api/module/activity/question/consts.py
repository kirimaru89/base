class QuestionType:
    SINGLE = 1
    MULTIPLE = 2


QUESTION_TYPE_CHOICES = (
    (QuestionType.SINGLE, "Single choice"),
    (QuestionType.MULTIPLE, "Multiple choices"),
)

QUESTION_TYPE_DICT = dict(QUESTION_TYPE_CHOICES)

QUESTION_TYPES = [{"value": k, "label": v} for k, v in QUESTION_TYPE_CHOICES]
