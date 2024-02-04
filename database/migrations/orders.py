from sqlalchemy import Column, Integer, ForeignKey, DateTime, String, BigInteger
from sqlalchemy.orm import relationship

from database.app import db


STATUS_CREATE = 'create'
STATUS_COMPLETED = 'completed'
STATUS_DECLINED = 'decline'


class Order(db.Model):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    status = Column(String)
    uc = Column(String)
    sum = Column(Integer)
    pubg_id = Column(BigInteger)
    created_at = Column(DateTime)
    paid_at = Column(DateTime)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship('User', back_populates='orders')
