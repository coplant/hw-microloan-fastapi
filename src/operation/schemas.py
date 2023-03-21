from datetime import datetime
from fileinput import filename
from typing import List
from xml.dom.domreg import registered

from fastapi import File, UploadFile
from pydantic import BaseModel


class UserData(BaseModel):
    user_id: int
    first_name: str
    middle_name: str
    last_name: str
    email: str
    registered_at: datetime


class OperatorData(BaseModel):
    passport_id: int
    filename: str
    number: str
    user: UserData

    class Config:
        orm_mode = True


class OperatorListData(BaseModel):
    user_info: List[OperatorData]


class FileSchema(BaseModel):
    file: UploadFile
