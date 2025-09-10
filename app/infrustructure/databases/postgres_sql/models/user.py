from sqlalchemy.orm import Mapped, mapped_column

from .base_model import BaseDBModel

class UserModel(BaseDBModel):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(unique=True)
    hashed_password: Mapped[str] = mapped_column(default='')
    first_name: Mapped[str] = mapped_column(index=True)
    last_name: Mapped[str] = mapped_column(index=True)
    is_active: Mapped[bool] = mapped_column(default=False)
