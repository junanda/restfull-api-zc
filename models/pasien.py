from sqlalchemy import String, DATE, Column, Integer, TEXT
from utils import Base


class Pasien(Base):
    __tablename__ = "pasiens"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    gender = Column(String(10))
    no_telp = Column(String(17))
    birthday = Column(DATE)
    address = Column(TEXT)
