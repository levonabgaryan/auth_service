import subprocess
from typing import Any


def run_alembic_migrations() -> subprocess.Popen[Any]:
    command = [
        "alembic",
        "upgrade",
        "head"
    ]
    return subprocess.Popen(command)