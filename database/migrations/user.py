from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

from database.app import db

STATUS_UNREGISTER = 'unregister'
STATUS_LOGOUT = 'logout'
STATUS_ACTIVE = 'active'
STATUS_BANNED = 'banned'


class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer)
    username = Column(String)
    role = Column(String)
    status = Column(String)
    pubg_id = Column(Integer)
    login = Column(String)
    password = Column(String)
    created_at = Column(DateTime)

    # userStats = relationship('UserStats', back_populates='user', uselist=False)
    orders = relationship('Orders', back_populates='user')
