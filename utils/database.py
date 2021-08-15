import os
from dotenv import load_dotenv
from sqlalchemy.ext.declarative import declarative_base

BASE_JADI = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_JADI, "../.env"))

SQLALCHEMY_DATABSE_URL = f"mysql+pymysql://{os.getenv('MARIADB_USERNAME')}:{os.getenv('MARIADB_PASSWORD')}@" \
                         f"{os.getenv('MARIADB_HOST')}/{os.getenv('DB_NAME')}?charset=utf8mb4"


Base = declarative_base()
