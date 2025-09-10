from dataclasses import dataclass
import re

from app.application.use_cases.user.exceptions import InvalidEmailFormat, InvalidPasswordFormat


@dataclass(frozen=True)
class CreateUserRequest:
    first_name: str
    last_name: str
    password: str
    email: str

    def __post_init__(self) -> None:
        self.__validate_email()
        self.__validate_password()

    def __validate_password(self) -> None:
        """
        Validates a password according to the rules:
        - At least 8 characters
        - At least one uppercase letter
        - At least one lowercase letter
        - At least one digit
        - At least one special character (@$!%*?&)
        """
        if len(self.password) < 8:
            raise InvalidPasswordFormat()

        pattern = re.compile(
            r"""
            ^                   # start of string
            (?=.*[a-z])         # at least one lowercase
            (?=.*[A-Z])         # at least one uppercase
            (?=.*\d)            # at least one digit
            (?=.*[@$!%*?&#])     # at least one special character
            [A-Za-z\d@$!%*?&#]{8,} # allowed characters, length >= 8
            $                   # end of string
            """,
            re.VERBOSE
        )

        if not pattern.match(self.password):
            raise InvalidPasswordFormat()

    def __validate_email(self) -> None:
        pattern = re.compile(
            r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        )

        if not pattern.match(self.email):
            raise InvalidEmailFormat(email_=self.email)


@dataclass(frozen=True)
class CreateUserResponse:
    user_id: str
