import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

class Configuration:
    @property
    def postgres_db_url(self) -> str:
        user = os.getenv('DB_USER')
        password = os.getenv('DB_PASSWORD')
        host = os.getenv('DB_HOST')
        port = os.getenv('DB_PORT')
        db_name = os.getenv('DB_NAME')
        return f'postgresql+asyncpg://{user}:{password}@{host}:{port}/{db_name}'
