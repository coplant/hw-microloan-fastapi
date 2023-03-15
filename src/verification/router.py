from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from starlette.responses import JSONResponse

from auth.config import current_user
from auth.models import User
from database import get_async_session
from verification.schemas import PhotoData, Passport

router = APIRouter(
    prefix="/verify",
    tags=["Verification"],
)


@router.post("/")
async def verify_user(passport_data: Passport,
                      user: User = Depends(current_user),
                      session: AsyncSession = Depends(get_async_session)):
    data = Passport(
        filename=passport_data.filename,
        content_type=passport_data.content_type,
        data=passport_data.file,
        number=passport_data.number
    )
    session.add(data)
    await session.commit()
    data = {"status": "success", "data": None, "detail": "Data committed"}
    return JSONResponse(status_code=status.HTTP_200_OK, content=data)
