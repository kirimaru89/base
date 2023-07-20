import re
from django.utils.translation import gettext_lazy as _


class PasswordService:
    @staticmethod
    def password_validate(password):
        password_validate_message = _(
            "Passwords must contain at least 8 characters in length, a minimum of 1 uppercase letter, a minimum of 1 numeric character"
        )
        password = password.strip()
        errors = []
        if len(password) < 8:
            errors.append(_("Make sure your password is at least 8 letters"))
        elif re.search("[0-9]", password) is None:
            errors.append(_("Make sure your password has a number in it"))
        elif re.search("[A-Z]", password) is None:
            errors.append(_("Make sure your password has a capital letter in it"))
        if errors:
            return [password_validate_message]
        return []
