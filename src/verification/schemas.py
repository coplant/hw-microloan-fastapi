from typing import Union

from fastapi import UploadFile, File
from pydantic import BaseModel


class Passport(BaseModel):
    number: Union[str, None]
    file: Union[UploadFile, None] = File(...)
