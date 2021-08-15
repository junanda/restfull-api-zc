import uvicorn
from fastapi import FastAPI
from router import pasien
from fastapi_sqlalchemy import DBSessionMiddleware
from utils.database import SQLALCHEMY_DATABSE_URL

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=SQLALCHEMY_DATABSE_URL)


@app.get("/")
async def index():
    return {'body': 'welcome learning FastApi'}


app.include_router(pasien.router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
