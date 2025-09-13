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
        if isinstance(self.value, OperationError):
            return self.value
        else:
            raise AttributeError(f"Instance of {type(self).__name__} has no attribute 'operation_error'")

    @property
    def success(self) -> T:
        if not isinstance(self.value, OperationError):
            return self.value
        else:
            raise AttributeError(f"Instance of {type(self).__name__} has no attribute 'success'")

    @property
    def is_success(self) -> bool:
        return not isinstance(self.value, OperationError)

    @classmethod
    def from_success(cls, value: T) -> Self:
        return cls(value=value)

    @classmethod
    def from_operation_error(cls, operation_error: OperationError) -> Self:
        return cls(value=operation_error)
