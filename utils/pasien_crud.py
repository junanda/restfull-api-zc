from sqlalchemy.orm import Session
from fastapi_sqlalchemy import db
from models import Pasien, Pasienbase


def get_pasien(pasien_id: int):
    return db.session.query(Pasien).filter(Pasien.id == pasien_id).first()


def get_pasiens(skip: int = 0, limit: int = 100):
    return db.session.query(Pasien).offset(skip).limit(limit).all()


def create_pasien( pasien: Pasienbase):
    db_pasien = Pasien(
        name=pasien.name,
        gender=pasien.gender,
        no_telp=pasien.no_telp,
        birthday=pasien.birthday,
        address=pasien.address
    )

    db.session.add(db_pasien)
    db.session.commit()
    db.session.refresh(db_pasien)
    return db_pasien


def update(data_update: Pasienbase, id_pasien: int):
    data_up = db.session.query(Pasien).get(id_pasien)
    data_up.name = data_update.name
    data_up.gender = data_update.gender
    data_up.no_telp = data_update.no_telp
    data_up.birthday = data_update.birthday
    data_up.address = data_update.address
    db.session.commit()


def delete(id_p: int):
    data_del = db.session.query(Pasien).get(id_p)
    db.session.delete(data_del)
    db.commit()
