from sqlalchemy import Column, Integer

from database.app import db


class Wallet(db.Model):
    __tablename__ = 'stats'

    id = Column(Integer, primary_key=True)
    uc = Column(Integer)
    sum = Column(Integer)
    users = Column(Integer)
