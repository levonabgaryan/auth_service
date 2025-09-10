from dataclasses import dataclass, field
from typing import Self, Any


@dataclass(frozen=True)
class OperationError:
    message: str
    error_code: str | None = field(default=None)
    details: dict[str, Any] | None = field(default=None)


@dataclass(frozen=True)
class OperationResult[T]:
    value: OperationError | T

    @property
    def operation_error(self) -> OperationError:
        assert isinstance(self.value, OperationError), "No operation success value"
        return self.value

    @property
    def success(self) -> T:
        assert not isinstance(self.value, OperationError), "No operation error value"
        return self.value

    @property
    def is_success(self) -> bool:
        return not isinstance(self.value, OperationError)

    @classmethod
    def from_success(cls, value: T) -> Self:
        return cls(value=value)

    @classmethod
    def from_operation_error(cls, operation_error: OperationError) -> Self:
        return cls(value=operation_error)

