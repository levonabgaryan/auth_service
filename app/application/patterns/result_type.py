from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class Error:
    message: str
    error_code: str | None = field(default=None)
    details: dict[str, Any] | None = field(default=None)


@dataclass(frozen=True)
class Result[T]:
    value: T | Error

    @property
    def is_success(self) -> bool:
        return not isinstance(self.value, Error)

    @property
    def success_value(self) -> T:
        if not isinstance(self.value, Error):
            return self.value
        else:
            raise AttributeError(f"Instance of {type(self).__name__} has no attribute 'success_value'")

    @property
    def error_value(self) -> Error:
        if isinstance(self.value, Error):
            return self.value
        else:
            raise AttributeError(f"Instance of {type(self).__name__} has no attribute 'error_value'")

    @classmethod
    def from_success(cls, value: T) -> "Result[T]":
        return cls(value=value)

    @classmethod
    def from_error(cls, error: Error) -> "Result[T]":
        return cls(value=error)
