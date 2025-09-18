from dataclasses import dataclass

from app.application.patterns.result_type import Error
from app.application.use_cases.user.create_user import CreateUserUseCase
from app.application.use_cases.user.dtos import CreateUserRequest, CreateUserResponse
from app.interface_adapters.patterns.operation_result import OperationResult, OperationError
from app.application.use_cases.user.exceptions import InvalidEmailFormat, InvalidPasswordFormat


@dataclass
class UserController:
    create_user_use_case: CreateUserUseCase

    async def create_user(
        self,
        first_name: str,
        last_name: str,
        email: str,
        password: str,
    ) -> OperationResult[dict[str, str] | OperationError]:
        try:
            request = CreateUserRequest(
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password
            )

        except (InvalidEmailFormat, InvalidPasswordFormat) as exc:
            return OperationResult(
                OperationError.from_main_exception(exc=exc)
            )

        result = await self.create_user_use_case.execute(request)
        if result.success_value:
            return OperationResult(operation_success_value={'user_id': str(result.success_value)})

        return OperationResult(
            OperationError(message=result.error_value.message)
        )

