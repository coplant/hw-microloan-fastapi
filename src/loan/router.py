from typing import Union

from fastapi import APIRouter, Depends, Query
from fastapi.encoders import jsonable_encoder
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from starlette.responses import JSONResponse

from database import get_async_session

from auth.config import current_user
from auth.models import User
from loan.models import Loan
from loan.schemas import LoanInfo, LoanAdd
from schemas import ResponseModel

router = APIRouter(
    prefix="/loans",
    tags=["Loans"],
)


@router.get("/", response_model=ResponseModel)
async def get_loans(user_id: Union[int, None] = None,
                    user: User = Depends(current_user),
                    session: AsyncSession = Depends(get_async_session)):
    if not user_id:
        user_id = user.id
    if user.id == user_id or user.is_superuser:
        query = select(Loan).filter_by(user_id=user_id)
        result = await session.execute(query)
        result = result.scalars().all()
        info = []
        for item in result:
            info.append(LoanInfo(id=item.id,
                                 amount=item.amount,
                                 period=item.period,
                                 status=item.status,
                                 is_active=item.is_active,
                                 creation_date=item.creation_date,
                                 end_date=item.end_date
                                 ))
        data = {"status": "success", "data": jsonable_encoder(info), "detail": None}
        return JSONResponse(status_code=status.HTTP_200_OK, content=data)
    else:
        data = {"status": "error", "data": None, "detail": "Forbidden"}
        return JSONResponse(status_code=status.HTTP_403_FORBIDDEN, content=data)


@router.post("/new", response_model=ResponseModel)
async def add_loan(item: LoanAdd,
                   user: User = Depends(current_user),
                   session: AsyncSession = Depends(get_async_session)):
    if user.is_active:
        query = select(Loan).filter_by(user_id=user.id).filter_by(is_active=True)
        result = await session.execute(query)
        result = result.scalars().all()
        if result:
            data = {"status": "error", "data": None, "detail": "You already have an active loan"}
            return JSONResponse(status_code=status.HTTP_403_FORBIDDEN, content=data)
        else:
            if not user.is_verified:
                data = {"status": "error", "data": None, "detail": "You are not verified"}
                return JSONResponse(status_code=status.HTTP_307_TEMPORARY_REDIRECT, content=data)
            else:
                stmt = Loan(period=item.period, amount=item.amount, user_id=user.id)
                session.add(stmt)
                await session.commit()
                data = {"status": "success",
                        "data": jsonable_encoder(LoanAdd(period=item.period, amount=item.amount)),
                        "detail": "Loan request sent"}
                return JSONResponse(status_code=status.HTTP_200_OK, content=data)
