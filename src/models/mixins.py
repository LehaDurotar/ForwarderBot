from sqlalchemy import Column, DateTime
from sqlalchemy.orm import declared_attr
from sqlalchemy.sql import func


class HasServerDefaultField(object):
    @declared_attr
    def __mapper_args__(cls) -> dict:
        return {"eager_defaults": True}


class TimestampMixin(HasServerDefaultField):
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_onupdate=func.now())
