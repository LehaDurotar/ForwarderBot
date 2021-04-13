from typing import Generator
from contextlib import asynccontextmanager

from loguru import logger
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

from src.settings import POSTGRES_URI

engine = create_async_engine(POSTGRES_URI, echo=True)
SessionLocal = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


async def session_local() -> Generator:
    """
    Открывает новую сессию, все запросы к бд выполняются в рамках этой сессии
    """
    db = SessionLocal()
    try:
        yield db
    except Exception as err:
        logger.error(f"DB error: {err}")
        await db.rollback()
    finally:
        await db.close()
