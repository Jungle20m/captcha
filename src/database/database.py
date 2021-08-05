from enum import auto
from urllib.parse import quote_plus as urlquote

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.core.config import DB_NAME, DB_HOST, DB_PORT, DB_USER, DB_PASSWORD
from src.core.config import POOL_SIZE

DATABASE_URL = f'mariadb+mariadbconnector://{DB_USER}:{urlquote(DB_PASSWORD)}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

engine = create_engine(DATABASE_URL, pool_size=POOL_SIZE,  pool_pre_ping=True)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)