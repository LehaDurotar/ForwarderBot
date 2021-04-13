import uuid

from sqlalchemy import Enum, Column, String, BigInteger, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID, JSONB

from src.models.enums import WallTypeEnum
from src.database.base_class import Base


class Wall(Base):
    id = Column(UUID(as_uuid=True), primary_key=True, unique=True, default=uuid.uuid4)
    source_id = Column(BigInteger, nullable=False)
    url = Column(String(255))
    short_name = Column(String(30))
    type = Column(Enum(WallTypeEnum))
    extra_data = Column(JSONB, default={})
    bucket_id = Column(UUID(as_uuid=True), ForeignKey("buckets.id", onupdate="CASCADE", ondelete="CASCADE"))
    linked_chat_id = Column(
        UUID(as_uuid=True), ForeignKey("chats.id", onupdate="CASCADE", ondelete="CASCADE")
    )
    wall_arg_id = Column(
        UUID(as_uuid=True), ForeignKey("wallargs.id", onupdate="CASCADE", ondelete="CASCADE")
    )

    linked_chat = relationship("Chat", back_populates="walls")
    bucket = relationship("Bucket", back_populates="walls")
    wall_arg = relationship("WallArg", back_populates="walls")
