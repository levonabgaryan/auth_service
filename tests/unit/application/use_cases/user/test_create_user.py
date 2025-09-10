from unittest.mock import Mock, AsyncMock

import pytest

from app.application.use_cases.user.create_user import CreateUserUseCase
from app.application.use_cases.user.dtos import CreateUserRequest
from app.application.use_cases.user.exceptions import InvalidPasswordFormat, InvalidEmailFormat


@pytest.mark.parametrize(
    "dto_data",
    [
        {"first_name": "test", "last_name": "test", "email": "test1@gmail.com", "password": "Aa123123#"}
    ]
)
@pytest.mark.asyncio
async def test_create_user_use_case_with_valid_dto(dto_data):
    # Arrange
    valid_request_dto = CreateUserRequest(**dto_data)
    user_repo = AsyncMock()
    password_hasher = Mock()
    use_case = CreateUserUseCase(user_repository=user_repo, password_hasher=password_hasher)

    # Act
    result = await use_case.execute(valid_request_dto)

    # Assert
    assert result.is_success
    user_repo.add.assert_called_once()
    password_hasher.hash_password.assert_called_once()
