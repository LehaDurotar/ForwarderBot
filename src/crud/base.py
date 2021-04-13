from typing import Any, Dict, Type, Generic, TypeVar, Optional

from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.base_class import Base

ModelType = TypeVar("ModelType", bound=Base)


class CRUDBase(Generic[ModelType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    async def get_object(self, session: AsyncSession, filters: Dict[str, Any]) -> Optional[ModelType]:
        query = await session.execute(select(self.model).filter_by(**filters))
        await session.commit()

        return query.scalars().first()

    async def get_multi_objects(
        self, session: AsyncSession, order_by: list = None, offset: int = 0, limit: int = 100
    ):
        if not order_by:
            order_by = []
        query = await session.execute(select(self.model).order_by(*order_by).offset(offset).limit(limit))
        await session.commit()

        return query.scalars().all()

    async def create(self, session: AsyncSession, obj_data: Dict[str, Any]) -> ModelType:
        db_obj = self.model(**obj_data)

        session.add(db_obj)
        await session.commit()
        await session.refresh(db_obj)

        return db_obj

    async def update(self, session: AsyncSession, db_obj: ModelType, obj_data: Dict[str, Any]) -> ModelType:
        update_data = self.model(**db_obj)

        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])

        session.add()
        await session.commit()
        await session.refresh(db_obj)

        return db_obj

    async def delete(self, session: AsyncSession, filters: Dict[str, Any]):
        db_obj = await self.get_object(session=session, filters=filters)

        await session.delete(db_obj)
        await session.commit()
