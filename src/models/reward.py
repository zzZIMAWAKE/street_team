from sqlalchemy import Column, Integer, String, Sequence
from .base import Base


class Reward(Base):
    __tablename__ = 'reward'
    id = Column(Integer, Sequence('reward_id_seq'), primary_key=True)
    name = Column(String())
    category = Column(String())
    points = Column(Integer())
    max_per_user = Column(Integer())
    global_max = Column(Integer())
