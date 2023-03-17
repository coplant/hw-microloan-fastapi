from typing import Union, Any

from pydantic import BaseModel


class ResponseModel(BaseModel):
    status: str
    data: Union[str, bytes, Any]
    details: Union[Any, None]
