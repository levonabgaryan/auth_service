from dataclasses import dataclass

from app.application.use_cases.user.create_user import CreateUserUseCase
from app.entrypoint.containers.repositories import RepositoryContainer
from app.infrustructure.bcrypt_password_hasher import BcryptPasswordHasher

@dataclass
class UseCaseContainer:
    repositories: RepositoryContainer

    def __post_init__(self) -> None:
        self.create_user_use_case = CreateUserUseCase(user_repository=self.repositories.user_repository, password_hasher=BcryptPasswordHasher())
