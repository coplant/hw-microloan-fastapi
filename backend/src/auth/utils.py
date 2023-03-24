from fastapi import Depends, HTTPException
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from auth.models import User
from database import get_async_session
from verification.utils import get_by_number


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)


async def validate_passport(passport: str) -> None:
    if not passport.isnumeric():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid passport number characters",
        )
    if len(passport) != 10:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid passport number length",
        )
    if await get_by_number(passport):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="This passport number is already in use",
        )
