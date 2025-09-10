from typing import Annotated, Any

from fastapi import APIRouter
from fastapi.params import Depends

from app.interface_adapters.controllers.user_controller import UserController
from .schemas import CreateUserSchema
from app.entrypoint.containers.app_container import app_container

router: APIRouter = APIRouter(prefix="/users", tags=["users"])


def get_user_controller() -> UserController:
    return app_container.controllers.user_controller


@router.post("/create-user")
async def create_user(
    body: CreateUserSchema,
    user_controller: Annotated[UserController, Depends(get_user_controller)],
) -> Any:
    rs = user_controller.create_user(
        first_name=body.first_name,
        last_name=body.last_name,
        email=str(body.email),
        password=body.password
    )

    if rs.is_success:
        print(rs.value, '++++++++++++++++++++++++++')
        return 200

    return rs.value
