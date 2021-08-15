from pydantic import BaseModel
from datetime import date


class Pasienbase(BaseModel):
    name: str
    gender: str
    no_telp: str
    birthday: date = None
    address: str

    class Config:
        orm_mode = True