from pydantic import BaseModel


class PhotoData(BaseModel):
    filename: str
    content_type: str
    file: bytes


class Passport(PhotoData):
    number: str
