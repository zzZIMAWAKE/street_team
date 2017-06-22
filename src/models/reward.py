from sqlalchemy import Column, Integer, String, Sequence, BigInteger
from .base import Base


class Reward(Base):
    __tablename__ = 'reward'
    id = Column(BigInteger, Sequence('reward_id_seq'), primary_key=True)
    name = Column(String())
    category = Column(String())
    points = Column(Integer())
    max_per_user = Column(Integer())
    global_max = Column(Integer())
