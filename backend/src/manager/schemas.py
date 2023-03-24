from datetime import datetime
from typing import List

from pydantic import BaseModel
from schemas import ResponseModel


class Loan(BaseModel):
    id: int
    user_id: int
    amount: int
    period: int
    is_active: bool
    status: str
    creation_date: datetime
    end_date: datetime


class LoansProcess(ResponseModel):
    data: List[Loan]


class History(BaseModel):
    id: int
    first_name: str
    last_name: str
    middle_name: str
    passport: str
    period: int
    amount: int
    is_active: bool


class LoanHistory(ResponseModel):
    data: List[History]
