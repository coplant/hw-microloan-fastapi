from datetime import datetime
from typing import Union

from pydantic import BaseModel, PositiveInt


class LoanAdd(BaseModel):
    period: PositiveInt
    amount: PositiveInt


class LoanInfo(LoanAdd):
    id: int
    status: str
    is_active: bool
    creation_date: datetime
    end_date: Union[datetime, None]
