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
        assert not isinstance(self.value, Error), "No success value"
        return self.value

    @property
    def error_value(self) -> Error:
        assert isinstance(self.value, Error), "No error value"
        return self.value

    @classmethod
    def from_success(cls, value: T) -> "Result[T]":
        return cls(value=value)

    @classmethod
    def from_error(cls, error: Error) -> "Result[T]":
        return cls(value=error)
