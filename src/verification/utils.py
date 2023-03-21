from sqlalchemy import select

from database import async_session_maker
from verification.models import Passport


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
