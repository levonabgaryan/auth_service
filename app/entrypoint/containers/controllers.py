from dataclasses import dataclass

from app.entrypoint.containers.use_cases import UseCaseContainer
from app.interface_adapters.controllers.user_controller import UserController


@dataclass
class ControllerContainer:
    use_cases: UseCaseContainer

    def __post_init__(self) -> None:
        self.user_controller = UserController(create_user_use_case=self.use_cases.create_user_use_case)
        