from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import declarative_base

from alembic_fake.config import DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_FAKE

Base_fake = declarative_base()

FAKE_DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_FAKE}"
fake_engine = create_async_engine(FAKE_DATABASE_URL)
fake_session_maker = async_sessionmaker(fake_engine, expire_on_commit=False)


async def get_fake_session() -> AsyncGenerator[AsyncSession, None]:
    async with fake_session_maker() as session:
        yield session
