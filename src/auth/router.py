from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from starlette.responses import JSONResponse

from auth.config import fastapi_users, auth_backend, current_user
from auth.models import User
from auth.schemas import UserRead, UserCreate, UserUpdate
from database import get_async_session
from loan.models import Loan
from loan.schemas import LoanInfo

router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
)
router.include_router(fastapi_users.get_auth_router(auth_backend))
router.include_router(fastapi_users.get_register_router(UserRead, UserCreate))

users = APIRouter(
    prefix="/users",
    tags=["Users"],
)

# Get loan data in /me route
# @users.get("/me")
# async def read_user(user: User = Depends(current_user),
#                     session: AsyncSession = Depends(get_async_session)):
#     query = select(Loan).filter_by(user_id=user.id)
#     result = await session.execute(query)
#     result = result.scalars().all()
#     info = []
#     for item in result:
#         info.append(LoanInfo(id=item.id,
#                              amount=item.amount,
#                              period=item.period,
#                              status=item.status,
#                              is_active=item.is_active,
#                              creation_date=item.creation_date,
#                              end_date=item.end_date
#                              ))
#     data = {"status": "success", "data": jsonable_encoder(info), "detail": None}
#     return JSONResponse(status_code=status.HTTP_200_OK, content=data)


users.include_router(fastapi_users.get_users_router(UserRead, UserUpdate))
