from typing import Any, Dict, Optional

from sqlalchemy.ext.asyncio import AsyncSession

from src.crud.base import CRUDBase
from src.models.subscribers import Subscriber


class CRUDSubscriber(CRUDBase[Subscriber]):
    async def create(self, session: AsyncSession, subscriber_data: Dict[str, Any]) -> Subscriber:
        subscriber_obj = await super().create(session=session, obj_data=subscriber_data)

        return subscriber_obj

    async def create_with_user(
        self,
        session: AsyncSession,
        user_tg_id: int,
    ) -> Optional[Subscriber]:
        user_obj = await super().get_object(session=session, filters={"user": ""})

        return user_obj

    async def update(
        self,
        session: AsyncSession,
        subscriber_obj: Subscriber,
        subscriber_data: Dict[str, Any],
    ) -> Subscriber:
        subscriber_update_obj = await super().update(
            session=session, db_obj=subscriber_obj, obj_data=subscriber_data
        )

        return subscriber_update_obj


subscriber = CRUDSubscriber(Subscriber)
