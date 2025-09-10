from typing import override

from app.application.ports.repositories.user_repository import UserRepository
from app.domain.entities.user.user_entity import User
from ..databases.postgres_sql.models.user import UserModel
from app.infrustructure.databases.postgres_sql.postgres_sql_based import PostgresSQLBasedRepository


class PostgresPostgresSQLUserRepository(UserRepository, PostgresSQLBasedRepository):

    @override
    async def add(self, user: User) -> None:
        to_add = UserModel(
            id=user.id_,
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            hashed_password=user.get_hashed_password_for_persistence()
        )
        async with self._connector.session() as session:
            session.add(to_add)
            await session.commit()
            await session.refresh(to_add)
