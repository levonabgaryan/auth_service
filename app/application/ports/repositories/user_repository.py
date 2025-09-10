from abc import ABC, abstractmethod

from app.domain.entities.user.user_entity import User

class UserRepository(ABC):
    @abstractmethod
    async def add(self, user: User) -> None:
        pass
