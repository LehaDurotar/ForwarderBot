import uuid

from sqlalchemy import Enum, Column, BigInteger, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from src.models.enums import ChatTypeEnum
from src.database.base_class import Base


class Chat(Base):
    id = Column(UUID(as_uuid=True), primary_key=True, unique=True, default=uuid.uuid4)
    telegram_id = Column(BigInteger, nullable=False)
    type = Column(Enum(ChatTypeEnum))

    linked_wall_id = Column(
        UUID(as_uuid=True), ForeignKey("walls.id", onupdate="CASCADE", ondelete="CASCADE")
    )
    bucket_id = Column(UUID(as_uuid=True), ForeignKey("buckets.id", onupdate="CASCADE", ondelete="CASCADE"))

    linked_wall = relationship("Wall", back_populates="chats")
    bucket = relationship("Bucket", back_populates="chats")
