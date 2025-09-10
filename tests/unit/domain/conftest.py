import pytest

from app.domain.entities.user.user_entity import User


@pytest.fixture
def user(
    first_name: str,
    last_name: str,
    email: str,
    hashed_password: str,
) -> User:
    return User(
        first_name=first_name,
        last_name=last_name,
        email_init=email,
        hashed_password=hashed_password
    )
