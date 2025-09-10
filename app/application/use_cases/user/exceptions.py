from app.main_exception import MainException
from .error_codes import INVALID_EMAIL_FORMAT, INVALID_PASSWORD_FORMAT


class InvalidEmailFormat(MainException):
    def __init__(self, email_: str) -> None:
        super().__init__(
            message='Email format is invalid',
            error_code=INVALID_EMAIL_FORMAT,
            details={'email': email_}
        )


class InvalidPasswordFormat(MainException):
    def __init__(self) -> None:
        super().__init__(
            message="Password must be at least 8 characters long, "
                    "contain uppercase, lowercase, digit, and special character",
            error_code=INVALID_PASSWORD_FORMAT,
        )
