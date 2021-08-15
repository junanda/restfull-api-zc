import uvicorn
from fastapi import FastAPI
from router import pasien

app = FastAPI()


@app.get("/")
async def index():
    return {'body': 'welcome learning FastApi'}


app.include_router(pasien.router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
