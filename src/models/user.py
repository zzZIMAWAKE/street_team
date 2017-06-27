from sqlalchemy import Column, Integer
from .base import Base


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    points = Column(Integer, default=0)
