from dataclasses import dataclass, field, InitVar
from typing import Any, Self

from app.main_exception import MainException


@dataclass(frozen=True)
class Error:
    message: str
    error_code: str | None = field(default=None)
    details: dict[str, Any] | None = field(default=None)

    @classmethod
    def from_main_exception(cls, exc: MainException) -> Self:
        return cls(
            message=exc.message,
            error_code=exc.error_code,
            details=exc.details
        )


@dataclass(frozen=True)
class Result[T]:
    success_value: T | None = field(default=None)
    error_value_: Error | None = field(default=None)

    @property
    def error_value(self) -> Error:
        """Property exists purely for static type checkers.
        Exposing a single attribute via a property is enough for type checking."""
        if self.error_value is None:
            raise AttributeError(f"Instance of {type(self).__name__} has no attribute 'error_value'")
        return self.error_value
