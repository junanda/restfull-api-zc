from sqlalchemy.orm import Session
from models import Pasien, Pasienbase


def get_pasien(db: Session, pasien_id: int):
    return db.query(Pasien).filter(Pasien.id == pasien_id).first()


def get_pasiens(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Pasien).offset(skip).limit(limit).all()


def create_pasien(db: Session, pasien: Pasienbase):
    db_pasien = Pasien(
        name=pasien.name,
        gender=pasien.gender,
        no_telp=pasien.no_telp,
        birthday=pasien.birthday,
        address=pasien.address
    )

    db.add(db_pasien)
    db.commit()
    db.refresh(db_pasien)
    return db_pasien


def update(db: Session, data_update: Pasienbase, id_pasien: int):
    data_up = db.query(Pasien).get(id_pasien)
    data_up.name = data_update.name
    data_up.gender = data_update.gender
    data_up.no_telp = data_update.no_telp
    data_up.birthday = data_update.birthday
    data_up.address = data_update.address
    db.commit()


def delete(db: Session, id_p: int):
    data_del = db.query(Pasien).get(id_p)
    db.delete(data_del)
    db.commit()
