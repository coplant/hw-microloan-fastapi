from typing import Optional
from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    id: int
    first_name: str
    middle_name: str
    last_name: str
    role_id: int
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False

    class Config:
        orm_mode = True


class UserCreate(schemas.BaseUserCreate):
    first_name: str
    middle_name: str
    last_name: str
    password: str
    passport: str


class UserUpdate(schemas.BaseUserUpdate):
    first_name: str
    middle_name: str
    last_name: str
    password: str
    passport: str
