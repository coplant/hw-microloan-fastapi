from sqlalchemy import select

from database import async_session_maker
from verification.models import Passport


async def get_by_number(number: str):
    async with async_session_maker() as session:
        query = select(Passport).filter_by(number=number)
        passport = await session.execute(query)
        return passport.first()
