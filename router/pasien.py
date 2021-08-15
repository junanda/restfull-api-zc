import pymysql
from fastapi import APIRouter
from utils import pasien_crud
from models import Pasienbase

router = APIRouter()


@router.get('/pasiens')
async def get_user():
    data_all = pasien_crud.get_pasiens()
    if len(data_all) > 0:
        ps_dat = data_all
    else:
        ps_dat = "Mohon Maaf data tidak ada"
    data = {
        'status': "Success",
        'body': ps_dat
    }
    return data


@router.post('/pasiens')
async def create_pasien(data: Pasienbase):
    db_pasien = pasien_crud.create_pasien(pasien=data)
    data = {
        'status': "success",
        'body': db_pasien
    }
    return data


@router.get('/pasiens/{idp}')
async def get_pasien(idp: int):
    db_person = pasien_crud.get_pasien(pasien_id=idp)
    data = {
        'status': 'success',
        'body': db_person
    }
    return data


@router.put('/pasiens/{idpasien}')
async def update_pasien(idpasien: int, data_update: Pasienbase):
    pasien_crud.update(data_update=data_update, id_pasien=idpasien)
    data = {
        'status': 'success',
        'body': 'Pasien berhasil di update'
    }
    return data


@router.delete('/pasiens/{iddel}')
async def delete_pasien(iddel: int):
    try:
        pasien_crud.delete(id_p=iddel)
        data_info = f"Pasien dengan id {iddel} berhasil dihapus"
    except pymysql.Error:
        data_info = "Gagal menghapus data pasien"
    data = {
        'status': 'success',
        'body': data_info
    }
    return data
