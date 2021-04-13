from uuid import UUID
from typing import Optional

from pydantic import BaseModel


class UserBase(BaseModel):
    is_superuser: bool = False
    telegram_id: Optional[int] = None


class CreateUser(UserBase):
    telegram_id: int


class UpdateUser(UserBase):
    pass


class UserInDB(UserBase):
    id: Optional[UUID] = None

    class Config:
        orm_mode = True
