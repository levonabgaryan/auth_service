from dataclasses import dataclass, field, InitVar

from app.domain.entities.base_entity import Entity


@dataclass
class User(Entity):
    first_name: str
    last_name: str

    email_init: InitVar[str]
    hashed_password: InitVar[str]

    __email: str = field(init=False)
    __hashed_password: str = field(init=False)
    __is_active: bool = field(default=False, init=False)

    def __post_init__(self, email: str, hashed_password: str) -> None:
        self.__email = email
        self.__hashed_password = hashed_password

    def get_hashed_password_for_persistence(self) -> str:
        return self.__hashed_password

    @property
    def email(self) -> str:
        return self.__email
