from typing import Union, Any

from pydantic import BaseModel


class PassportRead(BaseModel):
    number: str

    class Config:
        orm_mode = True


class ResponseModel(BaseModel):
    status: str
    data: Union[str, bytes, Any]
    details: Union[Any, None]
