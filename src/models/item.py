from sqlalchemy import Column, BigInteger, Sequence
from .base import Base


class Item(Base):
    __tablename__ = 'item'
    id = Column(BigInteger, Sequence('item_id_seq'), primary_key=True)
