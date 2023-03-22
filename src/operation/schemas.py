from datetime import datetime
from typing import List
from fastapi import UploadFile
from pydantic import BaseModel

from schemas import ResponseModel


class UserData(BaseModel):
    user_id: int
    first_name: str
    middle_name: str
    last_name: str
    email: str
    registered_at: datetime


class PassportData(BaseModel):
    passport_id: int
    filename: str
    user: UserData
    number: str


class FileSchema(BaseModel):
    file: UploadFile


class GetOperatorData(ResponseModel):
    data: List[PassportData]
