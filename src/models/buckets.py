import uuid

from sqlalchemy import Column, ForeignKey, SmallInteger
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from src.database.base_class import Base


class Bucket(Base):
    id = Column(UUID(as_uuid=True), primary_key=True, unique=True, default=uuid.uuid4)
    max_count = Column(SmallInteger, default=10)
    subscriber_id = Column(
        UUID(as_uuid=True), ForeignKey("subscribers.id", onupdate="CASCADE", ondelete="CASCADE")
    )

    subscriber = relationship("Subscriber", back_populates="buckets")
    chats = relationship("Chat", back_populates="buckets")
    walls = relationship("Wall", back_populates="buckets")
