# RestFull - API ZC

Stack tech:
1. FastAPI
2. SqlAlchemy
3. Alembic
4. MariaDB

For Running you must install dependency for this RestAPI using command

`pip install -r requirement.txt`

make .env file and initial variable

`MARIADB_HOST`, `MARIADB_USERNAME`, `MARIADB_PASSWORD`, `DB_NAME`

Create database and make migration with command

`alembic revision --autogenerate -m “create or generate table"`

`alembic upgrade head`

for running, type command

`python main.py` or `uvicorn ain:app --reload`

endpoint `http://127.0.0.1:8000/pasiens`

Docuementasi API (Swagger) : `http://127.0.0.1:8000/docs`
