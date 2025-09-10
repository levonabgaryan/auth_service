from app.configurations.configuration import Configuration
from app.infrustructure.databases.postgres_sql.postgres_sql_database_connector import PostgresSQLDatabaseConnector


class PostgresSQLBasedRepository:
    def __init__(self) -> None:
        config = Configuration()
        self._connector = PostgresSQLDatabaseConnector(config=config)
