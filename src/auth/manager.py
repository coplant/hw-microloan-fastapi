from typing import Optional, Union
from fastapi import Depends, Request, HTTPException
from fastapi_users import BaseUserManager, IntegerIDMixin, exceptions, models, schemas, InvalidPasswordException
from starlette import status

from auth.models import User
from auth.schemas import UserCreate
from auth.utils import get_user_db, validate_passport

from config import SECRET
from database import async_session_maker
from verification.models import Passport


class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET

    async def on_after_register(self, user: User, request: Optional[Request] = None, data: dict = None):
        async with async_session_maker() as session:
            passport_raw = data.pop("passport")
            passport = Passport(number=passport_raw, user_id=user.id)
            session.add(passport)
            await session.commit()
            return passport

    async def validate_password(
            self,
            password: str,
            user: Union[UserCreate, User],
    ) -> None:
        try:
            if len(password) < 8:
                raise InvalidPasswordException(
                    reason="Password should be at least 8 characters"
                )
            if user.email.lower() in password.lower() or password.lower() in user.email.lower():
                raise InvalidPasswordException(
                    reason="Password should not contain e-mail"
                )
        except InvalidPasswordException as exc:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=exc.reason,
            )

    async def create(self, user_create: UserCreate, safe: bool = False, request: Optional[Request] = None) -> models.UP:
        await self.validate_password(user_create.password, user_create)
        existing_user = await self.user_db.get_by_email(user_create.email)
        if existing_user is not None:
            raise exceptions.UserAlreadyExists()

        user_dict = (
            user_create.create_update_dict()
            if safe
            else user_create.create_update_dict_superuser()
        )
        password = user_dict.pop("password")
        user_dict["hashed_password"] = self.password_helper.hash(password)
        user_dict["role_id"] = 0
        passport = user_dict.pop("number")
        await validate_passport(passport)
        created_user = await self.user_db.create(user_dict)
        user_dict.update({"passport": passport})
        passport = await self.on_after_register(created_user, request=request, data=user_dict)
        created_user.passport = passport
        return created_user


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db=user_db)
