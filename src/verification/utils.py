from enum import Enum

from sqlalchemy import select

from database import async_session_maker
from verification.models import Passport


class Roles(Enum):
    admin = 100
    user = 0
    operator = 1
    manager = 2
    accountant = 3


async def get_by_number(number: str):
    async with async_session_maker.begin() as session:
        query = select(Passport).filter_by(number=number)
        passport = await session.execute(query)
        return passport.unique().scalar()


async def get_by_id(user_id: int):
    async with async_session_maker.begin() as session:
        query = select(Passport).filter_by(user_id=user_id)
        passport = await session.execute(query)
        return passport.unique().scalar()
