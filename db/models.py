from sqlalchemy import create_engine, Column, Integer, String, BigInteger
from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key = True)
    tg_id = Column(String)
    name = Column(String)
    phone = Column(String)
    email = Column(String)

