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

users.include_router(fastapi_users.get_users_router(UserRead, UserUpdate))
