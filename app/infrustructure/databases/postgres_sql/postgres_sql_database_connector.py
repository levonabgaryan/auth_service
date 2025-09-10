from contextlib import asynccontextmanager
from typing import AsyncIterator, Self

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

from app.configurations.configuration import Configuration


class PostgresSQLDatabaseConnector:
    _instance: Self | None = None
    _initialized: bool = False

    def __new__(cls, *args, **kwargs) -> Self:
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, config: Configuration) -> None:
        if not self._initialized:
            self.__engine = create_async_engine(config.postgres_db_url)
            self.__async_session = async_sessionmaker(
                bind=self.__engine,
                class_=AsyncSession,
                expire_on_commit=False
            )
            self._initialized = True

    @asynccontextmanager
    async def session(self) -> AsyncIterator[AsyncSession]:
        async with self.__async_session() as async_session_client:
            yield async_session_client

