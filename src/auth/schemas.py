from typing import Union
from fastapi_users import schemas
from schemas import PassportRead


class UserRead(schemas.BaseUser[int]):
    id: int
    email: str
    first_name: str
    middle_name: str
    last_name: str
    role_id: int
    passport: PassportRead
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False

    class Config:
        orm_mode = True


class UserCreate(schemas.BaseUserCreate):
    first_name: str
    middle_name: str
    last_name: str
    number: str


class UserUpdate(schemas.BaseUserUpdate):
    first_name: Union[str, None]
    middle_name: Union[str, None]
    last_name: Union[str, None]
