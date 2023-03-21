import os
from typing import Union

import fastapi_users.exceptions
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
from operation.schemas import OperatorData, OperatorListData, UserData, FileSchema
from operation.utils import get_unverified_users, is_unverified
from schemas import ResponseModel
from utils import Roles
from verification.config import IMAGE_DIR
from verification.models import Passport

router = APIRouter(
    prefix="/operation",
    tags=["Operator"],
)


@router.get("/", response_model=ResponseModel)
async def get_operator(user: User = Depends(current_user),
                       session: AsyncSession = Depends(get_async_session)):
    if user.is_active and (user.role_id == Roles.operator.value or user.is_superuser):
        query = select(Passport).options(joinedload(Passport.user))
        result = await session.execute(query)
        result = result.unique().scalars().all()
        users = await get_unverified_users(list[Passport](result))
        data = {"status": "success",
                "data": jsonable_encoder(
                    OperatorListData(
                        user_info=[OperatorData(
                            passport_id=user.id,
                            filename=user.filename,
                            number=user.number,
                            user=UserData(
                                user_id=user.user.id,
                                first_name=user.user.first_name,
                                middle_name=user.user.middle_name,
                                last_name=user.user.last_name,
                                email=user.user.email,
                                registered_at=user.user.registered_at,
                            )
                        ) for user in users]
                    )
                ),
                "detail": None}
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
