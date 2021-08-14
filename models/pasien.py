from sqlalchemy import String, DATE, Column, Integer, TEXT
from utils import Base


class Pasien(Base):
    __tablename__ = "pasiens"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    gender = Column(String)
    no_telp = Column(String)
    birthday = Column(DATE)
    address = Column(TEXT)
