from typing import List
from schemas import ResponseModel
from auth.schemas import UserRead
from manager.schemas import Loan


class Accountant(Loan):
    user: UserRead


class AccountantResponse(ResponseModel):
    data: List[Accountant]
