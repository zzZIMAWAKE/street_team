from sqlalchemy import Column, String, Sequence, BigInteger, Float, ForeignKey
from .base import Base

class Sale(Base):
    __tablename__ = 'sale'
    id = Column(BigInteger, Sequence('sale_id_seq'), primary_key=True)
    cost = Column(Float())
    currency = Column(String())
    user_id = Column(BigInteger(), ForeignKey('user.id'))
    item_id = Column(BigInteger(), ForeignKey('item.id'))
