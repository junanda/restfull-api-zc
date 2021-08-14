import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/api/v0.1/")
async def index():
    return {'body': 'welcome learning FastApi'}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)