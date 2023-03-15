from fastapi import UploadFile, File
from pydantic import BaseModel


class Passport(BaseModel):
    number: str
    file: UploadFile = File(...)

# class PassportUpload(Passport):
#     number: str
#     file: UploadFile = File(...)
