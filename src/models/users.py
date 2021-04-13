import uuid

from sqlalchemy import Column, Boolean, BigInteger
from sqlalchemy.orm import relationship
from sqlalchemy.sql import expression
from sqlalchemy.dialects.postgresql import UUID

from src.models.mixins import TimestampMixin
from src.database.base_class import Base


class User(Base, TimestampMixin):
    id = Column(UUID(as_uuid=True), primary_key=True, unique=True, default=uuid.uuid4)
    telegram_id = Column(BigInteger, unique=True, nullable=False)
    is_superuser = Column(Boolean, server_default=expression.false())

    subscriber = relationship("Subscriber", uselist=False, back_populates="users")
