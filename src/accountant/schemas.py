from datetime import datetime
from typing import List

from pydantic import BaseModel

from auth.schemas import UserRead
from manager.schemas import Loan
from schemas import ResponseModel


class Accountant(Loan):
    user: UserRead


class AccountantResponse(ResponseModel):
    data: List[Accountant]
