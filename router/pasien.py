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
