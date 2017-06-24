from sqlalchemy import Column, BigInteger, Integer
from .base import Base


class User(Base):
    __tablename__ = 'user'
    id = Column(BigInteger, primary_key=True)
    points = Column(Integer, default=0)
