from passlib.context import CryptContext

from app.application.ports.password_hasher import PasswordHasher

class BcryptPasswordHasher(PasswordHasher):

    def __init__(self) -> None:
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def hash_password(self, password: str) -> str:
        return self.pwd_context.hash(password)
