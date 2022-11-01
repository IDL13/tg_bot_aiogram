import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from datetime import datetime
from db.models import Base
from dotenv import load_dotenv

load_dotenv()

DATABASE = {
    'drivername': 'postgresql',
    'host': 'localhost',
    'port': '5432',
    'username': 'Admin_tgbot',
    'password': os.getenv('PASSWORD') ,
    'database': 'tgbot'
}

engine = create_engine(URL(**DATABASE))
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()