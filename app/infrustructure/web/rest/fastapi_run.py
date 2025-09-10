import subprocess
from typing import Any

from fastapi import FastAPI

from .http.routers.users.endpoints import router as users_router

app = FastAPI()

app.include_router(users_router)


def start_server() -> subprocess.Popen[Any]:
    command = [
        "uvicorn",
        "app.infrustructure.web.rest.fastapi_run:app",
        "--host", "0.0.0.0",  # from env
        "--port", "8000",  # from env
        "--reload",
    ]
    return subprocess.Popen(command)
