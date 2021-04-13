import uuid

from sqlalchemy import Column, Boolean, SmallInteger
from sqlalchemy.orm import relationship
from sqlalchemy.sql import expression
from sqlalchemy.dialects.postgresql import UUID

from src.database.base_class import Base


class WallArg(Base):
    id = Column(UUID(as_uuid=True), primary_key=True, unique=True, default=uuid.uuid4)
    sleep = Column(SmallInteger, default=30)
    fetch_count = Column(SmallInteger, default=2)
    admin_access = Column(Boolean, server_default=expression.false())

    walls = relationship("Wall", back_populates="wallargs")
