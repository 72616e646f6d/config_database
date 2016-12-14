from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Config(Base):
    __tablename__ = 'config'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

class Item(Base):
    __tablename__ = 'item'
    id = Column(Integer, primary_key=True)
    config_id = Column(ForeignKey('config.id'), nullable=True)
    key = Column(String)
    value = Column(String)
