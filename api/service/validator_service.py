from django.core.exceptions import ValidationError
from service.password_service import PasswordService


class ValidatorService:
    @staticmethod
    def password_validator(value):
        # errors = PasswordService.password_validate(value)
        # if errors:
        #     raise ValidationError(errors, code="invalid")
        pass

    @staticmethod
    def mobile_validator(value):
        pass
