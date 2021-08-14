from pydantic import BaseModel


class Pasienbase(BaseModel):
    name: str
    gender: str
    no_telp: str
    birthday: str
    address: str

    class Config:
        orm_mode = True