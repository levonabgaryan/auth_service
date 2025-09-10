import signal
import os
import sys
import subprocess
from typing import Any

from app.entrypoint.run_migrations import run_alembic_migrations
from app.infrustructure.web.rest.fastapi_run import start_server


def handle_keyboard_interrupt(process_: subprocess.Popen[Any]) -> None:
    try:
        process_.wait()
    except KeyboardInterrupt:
        print("\nServer stopped on Ctrl+C.")
    finally:
        print("End of process...")
        os.kill(process_.pid, signal.SIGTERM)
        sys.exit(0)


if __name__ == "__main__":
    run_alembic_migrations()
    process = start_server()
    handle_keyboard_interrupt(process)
