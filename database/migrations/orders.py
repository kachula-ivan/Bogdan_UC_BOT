from sqlalchemy import Column, Integer, ForeignKey, DateTime, String
from sqlalchemy.orm import relationship

from database.app import db


class Order(db.Model):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    status = Column(String)
    created_at = Column(DateTime)
    paid_at = Column(DateTime)
    user_id = Column(Integer, ForeignKey('users.id'))
    price_id = Column(Integer, ForeignKey('price.id'))

    user = relationship('User', back_populates='orders')
    price = relationship('Price', back_populates='orders')
