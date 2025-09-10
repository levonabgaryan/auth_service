from dataclasses import dataclass, field
from uuid import UUID, uuid4

@dataclass
class Entity:
    id_: UUID = field(default_factory=uuid4, init=False)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, type(self)):
            return False
        return self.id_ == other.id_
