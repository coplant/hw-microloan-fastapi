from datetime import datetime, timedelta
from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from starlette.responses import JSONResponse

from alembic_fake.fake_database import get_fake_session
from alembic_fake.models import FakeUser
from auth.config import current_user
from auth.models import User
from database import get_async_session
from loan.models import Loan
from manager.schemas import LoansProcess, LoanHistory, History
from schemas import ResponseModel
from utils import Roles, Status
from verification.models import Passport

router = APIRouter(
    prefix="/management",
    tags=["Manager"],
)


@router.get("/", response_model=LoansProcess)
async def get_manager(user: User = Depends(current_user),
                      session: AsyncSession = Depends(get_async_session)):
    if user.is_active and (user.role_id == Roles.manager.value or user.is_superuser):
        query = select(Loan).filter_by(is_active=True).filter_by(status=Status.consideration.value[1])
        result = await session.execute(query)
        result = result.scalars().all()
        data = {"status": "success",
                "data": jsonable_encoder([Loan(id=item.id,
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


@router.get('/history/{user_id}', response_model=LoanHistory)
async def get_history(user_id: int,
                      user: User = Depends(current_user),
                      fake_session: AsyncSession = Depends(get_fake_session),
                      session: AsyncSession = Depends(get_async_session)):
    if user.is_active and (user.role_id == Roles.manager.value or user.is_superuser):
        query = select(User).filter_by(id=user_id)
        result = await session.execute(query)
        result = result.unique().scalars().one_or_none()

        # checking credit history from fake database
        query = select(FakeUser).filter_by(passport=result.passport.number)
        result = await fake_session.execute(query)
        result = result.scalars().all()
        data = {"status": "success",
                "data": jsonable_encoder([History(id=user_id,
                                                  first_name=item.first_name,
                                                  last_name=item.last_name,
                                                  middle_name=item.middle_name,
                                                  passport=item.passport,
                                                  is_active=item.is_active,
                                                  period=item.period,
                                                  amount=item.amount
                                                  ) for item in result]),
                "detail": None}
        return JSONResponse(status_code=status.HTTP_200_OK, content=data)
    data = {"status": "error", "data": None, "detail": "Permission denied"}
    return JSONResponse(status_code=status.HTTP_403_FORBIDDEN, content=data)


@router.post('/response/{user_id}', response_model=ResponseModel)
async def response(user_id: int,
                   decision: bool,
                   user: User = Depends(current_user),
                   session: AsyncSession = Depends(get_async_session)):
    if user.is_active and (user.role_id == Roles.manager.value or user.is_superuser):
        query = select(Loan).filter_by(user_id=user_id).filter_by(is_active=True). \
            filter_by(status=Status.consideration.value[1])
        result = await session.execute(query)
        result = result.unique().scalars().one_or_none()
        if not result:
            data = {"status": "error", "data": None, "detail": "User not found"}
            return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content=data)
        result.is_active = decision
        if decision:
            result.status = Status.process.value[1]
            period = datetime.utcnow() + timedelta(days=result.period)
            result.end_date = period
        else:
            result.status = Status.rejected.value[1]
            result.end_date = result.creation_date
        session.add(result)
        await session.commit()
        data = {"status": "success", "data": decision, "detail": None}
        return JSONResponse(status_code=status.HTTP_200_OK, content=data)
    data = {"status": "error", "data": None, "detail": "Permission denied"}
    return JSONResponse(status_code=status.HTTP_403_FORBIDDEN, content=data)
