from fastapi import APIRouter
from auth.config import fastapi_users, auth_backend
from auth.schemas import UserRead, UserCreate, UserUpdate

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
