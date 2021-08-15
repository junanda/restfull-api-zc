from fastapi import APIRouter

router = APIRouter()


@router.get('/pasien')
async def get_user():
    data = {
        'status': "Success",
        'body': "Data pasiens"
    }
    return data
