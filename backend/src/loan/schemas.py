from datetime import datetime
from typing import Union, List

from pydantic import BaseModel, PositiveInt

from schemas import ResponseModel


class LoanAdd(BaseModel):
    period: PositiveInt
    amount: PositiveInt


class LoanInfo(LoanAdd):
    id: int
    status: str
    is_active: bool
    creation_date: datetime
    end_date: Union[datetime, None]


class GetLoanInfo(ResponseModel):
    data: List[LoanInfo]
