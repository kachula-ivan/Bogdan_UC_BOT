from sqlalchemy import Column, Integer, Float

from database.app import db


class Stats(db.Model):
    __tablename__ = 'stats'

    id = Column(Integer, primary_key=True)
    uc = Column(Integer, default=0)
    sum = Column(Float, default=0)
    orders = Column(Integer, default=0)
    users = Column(Integer, default=0)
