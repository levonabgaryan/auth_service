from dataclasses import dataclass

from app.infrustructure.databases.postgres_sql.postgres_sql_database_connector import PostgresSQLDatabaseConnector
from app.infrustructure.repositories.user_repository import PostgresPostgresSQLUserRepository


@dataclass
class RepositoryContainer:
    connector: PostgresSQLDatabaseConnector

    def __post_init__(self) -> None:
        self.user_repository = PostgresPostgresSQLUserRepository()
