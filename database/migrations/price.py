from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship

from database.app import db


class Price(db.Model):
    __tablename__ = 'price'

    id = Column(Integer, primary_key=True)
    uc = Column(String)
    sum = Column(Float)
    currency = Column(String)

    orders = relationship('Orders', back_populates='price')
