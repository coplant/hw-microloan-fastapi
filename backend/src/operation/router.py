import os
from typing import Union

from fastapi import APIRouter, Depends, Path
from fastapi.encoders import jsonable_encoder
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload
from starlette import status
from starlette.responses import JSONResponse, FileResponse

from auth.config import current_user
from auth.models import User
from database import get_async_session
from operation.schemas import PassportData, UserData, GetOperatorData
from operation.utils import get_unverified_users, is_unverified
from schemas import ResponseModel
from utils import Roles
from verification.config import IMAGE_DIR
from verification.models import Passport

router = APIRouter(
    prefix="/operation",
    tags=["Operator"],
)


@router.get("/", response_model=GetOperatorData)
async def get_operator(user: User = Depends(current_user),
                       session: AsyncSession = Depends(get_async_session)):
    if user.is_active and (user.role_id == Roles.operator.value or user.is_superuser):
        query = select(Passport).options(joinedload(Passport.user))
        result = await session.execute(query)
        result = result.unique().scalars().all()
        users = await get_unverified_users(list[Passport](result))
        info = []
        for item in users:
            info.append(PassportData(
                passport_id=item.id,
                filename=item.filename,
                number=item.number,
                user=UserData(
                    user_id=item.user.id,
                    first_name=item.user.first_name,
                    middle_name=item.user.middle_name,
                    last_name=item.user.last_name,
                    email=item.user.email,
                    registered_at=item.user.registered_at,
                )))
        data = {"status": "success", "data": jsonable_encoder(info), "detail": None}
        return JSONResponse(status_code=status.HTTP_200_OK, content=data)
    data = {"status": "error", "data": None, "detail": "Permission denied"}
    return JSONResponse(status_code=status.HTTP_403_FORBIDDEN, content=data)


@router.get("/photo/{filename}", response_class=FileResponse)
async def get_photo(user: User = Depends(current_user),
                    filename: str = Path(...),
                    session: AsyncSession = Depends(get_async_session)):
    if user.is_active and (user.role_id == Roles.operator.value or user.is_superuser):
        query = select(Passport.content_type).filter_by(filename=filename)
        result = await session.execute(query)
        result = result.unique().scalars().one_or_none()
        photo = IMAGE_DIR / filename
        return FileResponse(photo, headers={"Content-Type": result}, media_type=result)
    data = {"status": "error", "data": None, "detail": "Permission denied"}
    return JSONResponse(status_code=status.HTTP_403_FORBIDDEN, content=data)


@router.get("/verify/{user_id}", response_model=ResponseModel)
async def verify_by_id(user: User = Depends(current_user),
                       user_id: Union[int, None] = Path(...),
                       session: AsyncSession = Depends(get_async_session)):
    if user.is_active and (user.role_id == Roles.operator.value or user.is_superuser):
        stmt = select(User).filter_by(id=user_id)
        result = await session.execute(stmt)
        result = result.unique().scalars().one_or_none()
        if result:
            if await is_unverified(result):
                result.is_verified = True
                session.add(result)
                await session.commit()
                data = {"status": "success", "data": None, "detail": "User verified"}
                return JSONResponse(status_code=status.HTTP_200_OK, content=data)
    data = {"status": "error", "data": None, "detail": "Permission denied"}
    return JSONResponse(status_code=status.HTTP_403_FORBIDDEN, content=data)
