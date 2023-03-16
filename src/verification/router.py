import uuid
from http.client import HTTPException
from typing import Union

import aiofiles as aiofiles
from fastapi import APIRouter, Depends, File, UploadFile
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from starlette.responses import JSONResponse

from auth.config import current_user
from auth.models import User
from config import DEFAULT_CHUNK_SIZE
from database import get_async_session
from verification.config import IMAGE_DIR

router = APIRouter(
    prefix="/verify",
    tags=["Verification"],
)


@router.post("/")
async def verify_user(
        number: Union[str, None] = None,
        file: UploadFile = File(...),
        user: User = Depends(current_user),
        session: AsyncSession = Depends(get_async_session)):
    if not user.is_verified:
        if not number:
            if not user.passport.number:
                data = {"status": "error", "data": None, "detail": "Please provide a passport number"}
                return JSONResponse(status_code=status.HTTP_406_NOT_ACCEPTABLE, content=data)
            if user.passport.number:
                number = user.passport.number
        file.filename = f'{uuid.uuid4()}.jpg'
        file_path = IMAGE_DIR / file.filename
        async with aiofiles.open(file_path, "wb") as f:
            while chunk := await file.read(DEFAULT_CHUNK_SIZE):
                await f.write(chunk)

        # if user.passport:
        #     data = Passport(
        #         file.filename=data.file.filename,
        #         content_type=data.file.content_type,
        #         data=IMAGE_DIR / data.file.filename,  # todo: path to file
        #     )

        # data = Passport(
        #     filename=file.filename,
        #     content_type=file.content_type,
        #     data=IMAGE_DIR / file.filename,  # todo: path to file
        #     number=user.passport,
        #     user_id=user.id,
        # )

        # session.add(data)
        # await session.commit()

        data = {"status": "success", "data": None, "detail": "Data committed"}
        return JSONResponse(status_code=status.HTTP_200_OK, content=data)
    data = {"status": "success", "data": None, "detail": "You are already verified"}
    return JSONResponse(status_code=status.HTTP_200_OK, content=data)
