from app.infrustructure.databases.postgres_sql.postgres_sql_database_connector import PostgresSQLDatabaseConnector
from app.entrypoint.containers.controllers import ControllerContainer
from app.entrypoint.containers.repositories import RepositoryContainer
from app.entrypoint.containers.use_cases import UseCaseContainer
from app.configurations.configuration import Configuration


class ApplicationContainer:

    def __init__(self) -> None:
        self.configuration = Configuration()
        self.postgres_db_connector = PostgresSQLDatabaseConnector(config=self.configuration)
        self.repositories = RepositoryContainer(connector=self.postgres_db_connector)
        self.uses_cases = UseCaseContainer(repositories=self.repositories)
        self.controllers = ControllerContainer(use_cases=self.uses_cases)

app_container = ApplicationContainer()
