from dataclasses import dataclass, field
from typing import Self, Any

from app.main_exception import MainException


@dataclass(frozen=True)
class OperationError:
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
class OperationResult[T]:
    operation_success_value: T | None = field(default=None)
    operation_error_value_: OperationError | None = field(default=None)

    @property
    def operation_error_value(self) -> OperationError:
        """Property exists purely for static type checkers.
        Exposing a single attribute via a property is enough for type checking."""
        if self.operation_error_value_ is None:
            raise AttributeError(f"Instance of {type(self).__name__} has no attribute 'operation_error_value'")
        return self.operation_error_value_
