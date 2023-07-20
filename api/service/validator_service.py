from django.core.exceptions import ValidationError
from service.password_service import PasswordService


class ValidatorService:
    def password_validator(value):
        # errors = PasswordService.password_validate(value)
        # if errors:
        #     raise ValidationError(errors, code="invalid")
        pass

    def phone_number_validator(value):
        pass
