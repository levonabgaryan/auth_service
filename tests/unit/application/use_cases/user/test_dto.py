import pytest

from app.application.use_cases.user.dtos import CreateUserRequest
from app.application.use_cases.user.exceptions import InvalidEmailFormat


@pytest.mark.parametrize(
    "not_valid_data",
    [
        {"first_name": "test", "last_name": "test", "email": "not_valid_email", "password": "Aa123123#"}
    ]
)
@pytest.mark.asyncio
async def test_create_user_request_dto_should_raise_on_invalid_data(not_valid_data: dict[str, str]) -> None:
    # Arrange
    dto_data = not_valid_data

    # Act & Assert
    with pytest.raises(InvalidEmailFormat) as exc:
        CreateUserRequest(**dto_data)

    # Assert
    assert "[INVALID_EMAIL_FORMAT] Email format is invalid | Details: {'email': 'not_valid_email'}" == str(exc.value)
