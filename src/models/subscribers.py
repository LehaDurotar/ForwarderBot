import uuid

from sqlalchemy import Enum, Column, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import expression
from sqlalchemy.dialects.postgresql import UUID

from src.models.enums import SubscriberLevelEnum
from src.models.mixins import TimestampMixin
from src.database.base_class import Base


class Subscriber(Base, TimestampMixin):
    id = Column(UUID(as_uuid=True), primary_key=True, unique=True, default=uuid.uuid4)
    level = Column(Enum(SubscriberLevelEnum), nullable=False, server_default=SubscriberLevelEnum.guest)
    is_active = Column(Boolean, server_default=expression.false())
    expired_at = Column(DateTime(timezone=True))
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", onupdate="CASCADE", ondelete="CASCADE"))

    # one-to-one relations
    user = relationship("User", back_populates="subscribers")
    bucket = relationship("Bucket", uselist=False, back_populates="subscribers")
