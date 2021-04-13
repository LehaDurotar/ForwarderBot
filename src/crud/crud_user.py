from typing import Any, Dict, Optional

from sqlalchemy.ext.asyncio import AsyncSession

from src.crud.base import CRUDBase
from src.models.users import User


class CRUDUser(CRUDBase[User]):
    async def create(self, session: AsyncSession, user_data: Dict[str, Any]) -> User:
        user_obj = await super().create(session=session, obj_data=user_data)

        return user_obj

    async def update(self, session: AsyncSession, user_obj: User, user_data: Dict[str, Any]) -> User:
        user_update_obj = await super().update(session=session, db_obj=user_obj, obj_data=user_data)

        return user_update_obj


user = CRUDUser(User)
