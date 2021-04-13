from uuid import UUID
from typing import Optional
from datetime import datetime

from pydantic import BaseModel


class SubscriberBase(BaseModel):
    is_active: bool = False
    expired_at: Optional[datetime] = None


class SubscriberCreate(SubscriberBase):
    pass


class SubscriberUpdate(SubscriberBase):
    pass


class SubscriberInDB(SubscriberBase):
    id: Optional[UUID] = None
    user_id: Optional[UUID] = None
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True
