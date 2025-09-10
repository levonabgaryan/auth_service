from dataclasses import dataclass

from app.application.use_cases.user.create_user import CreateUserUseCase
from app.application.use_cases.user.dtos import CreateUserRequest
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
    ) -> OperationResult[dict[str, str]]:
        try:
            request = CreateUserRequest(
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password
            )

            result = await self.create_user_use_case.execute(request)
            if result.is_success:
                return OperationResult.from_success(
                    value={'user_id': result.success_value.user_id}
                )

            return OperationResult.from_operation_error(
                OperationError(
                    message=result.error_value.message,
                    error_code=result.error_value.error_code,
                    details=result.error_value.details
                )
            )

        except (InvalidEmailFormat, InvalidPasswordFormat) as exc:
            return OperationResult.from_operation_error(
                OperationError(
                    message=exc.message,
                    error_code=exc.error_code,
                    details=exc.details
                )
            )
