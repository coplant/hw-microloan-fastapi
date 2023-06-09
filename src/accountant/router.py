from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy import select
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from starlette.responses import JSONResponse

from accountant.models import Balance
from accountant.schemas import Accountant, AccountantResponse
from auth.config import current_user
from auth.models import User
from auth.schemas import UserRead
from database import get_async_session
from loan.models import Loan
from schemas import PassportRead
from utils import Roles, Status

router = APIRouter(
    prefix="/accountant",
    tags=["Accountant"],
)


@router.get("/", response_model=AccountantResponse)
async def get_accountant(user: User = Depends(current_user),
                         session: AsyncSession = Depends(get_async_session)):
    if user.is_active and (user.role_id == Roles.accountant.value or user.is_superuser):
        query = select(Loan).filter_by(is_active=True).filter_by(status=Status.process.value[1])
        result = await session.execute(query)
        result = result.unique().scalars().all()

        data = {"status": "success",
                "data": jsonable_encoder([Accountant(id=item.id,
                                                     user=UserRead(
                                                         id=item.user_id,
                                                         email=item.user.email,
                                                         first_name=item.user.first_name,
                                                         middle_name=item.user.middle_name,
                                                         last_name=item.user.last_name,
                                                         role_id=item.user.role_id,
                                                         passport=PassportRead(
                                                             number=item.user.passport.number).dict()
                                                     ).dict(),
                                                     user_id=item.user_id,
                                                     is_active=item.is_active,
                                                     creation_date=item.creation_date,
                                                     end_date=item.end_date,
                                                     status=item.status,
                                                     period=item.period,
                                                     amount=item.amount
                                                     ) for item in result]),
                "detail": None}
        return JSONResponse(status_code=status.HTTP_200_OK, content=data)

    data = {"status": "error", "data": None, "detail": "Permission denied"}
    return JSONResponse(status_code=status.HTTP_403_FORBIDDEN, content=data)


@router.post("/pay/{user_id}")
async def pay_loan(user_id: int,
                   user: User = Depends(current_user),
                   session: AsyncSession = Depends(get_async_session)):
    if user.is_active and (user.role_id == Roles.accountant.value or user.is_superuser):
        query = select(Loan).filter_by(user_id=user_id).filter_by(is_active=True).filter_by(
            status=Status.process.value[1])
        result = await session.execute(query)
        result = result.unique().scalar_one_or_none()
        if not result:
            data = {"status": "error", "data": None, "detail": "Loan not found"}
            return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content=data)
        if result.status == Status.approved.value[1]:
            data = {"status": "error", "data": None, "detail": "Loan already paid"}
            return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=data)
        stmt = insert(Balance).values(amount=-result.amount, user_id=user_id, loan_id=result.id)
        await session.execute(stmt)
        result.status = Status.approved.value[1]
        session.add(result)
        await session.commit()
        data = {"status": "success", "data": None, "detail": "Loan approved"}
        return JSONResponse(status_code=status.HTTP_200_OK, content=data)
    data = {"status": "error", "data": None, "detail": "Permission denied"}
    return JSONResponse(status_code=status.HTTP_403_FORBIDDEN, content=data)
