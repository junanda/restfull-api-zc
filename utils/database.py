import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABSE_URL = "mariadb+pymysql://{}:{}@{}/{}?charset=utf8mb4".format(os.getenv('MARIADB_USERNAME'),
                                                                                os.getenv('MARIADB_PASSWORD'),
                                                                                os.getenv('MARIADB_HOST'),
                                                                                os.getenv('DB_NAME'))

engine = create_engine(
    SQLALCHEMY_DATABSE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
