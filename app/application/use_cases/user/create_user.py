from dataclasses import dataclass

from app.domain.entities.user.user_entity import User
from app.application.ports.repositories.user_repository import UserRepository
from app.application.ports.password_hasher import PasswordHasher
from app.main_exception import MainException
from .dtos import CreateUserRequest, CreateUserResponse
from ...patterns.result_type import Result, Error


@dataclass
class CreateUserUseCase:
    user_repository: UserRepository
    password_hasher: PasswordHasher

    async def execute(self, request: CreateUserRequest) -> Result[CreateUserResponse | Error]:

        try:
            hashed_password = self.password_hasher.hash_password(request.password)
        except MainException as exc:
            return Result(
                Error.from_main_exception(exc=exc)
            )

        user = User(
            first_name=request.first_name,
            last_name=request.last_name,
            email_init=request.email,
            hashed_password=hashed_password
        )
        await self.user_repository.add(user)

        response = CreateUserResponse(user_id=str(user.id_))

        return Result(success_value=response)
