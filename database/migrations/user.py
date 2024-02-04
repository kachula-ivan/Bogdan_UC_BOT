from sqlalchemy import Column, Integer, String, DateTime, BigInteger
from sqlalchemy.orm import relationship

from database.app import db

STATUS_UNREGISTER = 'unregister'
STATUS_REGISTER = 'register'
STATUS_DECLINED = 'declined'
STATUS_LOGOUT = 'logout'
STATUS_ACTIVE = 'active'
STATUS_BANNED = 'banned'

ROLE_USER = 'user'
ROLE_ADMIN = 'admin'


class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    telegram_id = Column(BigInteger)
    first_name = Column(String)
    last_name = Column(String)
    username = Column(String)
    role = Column(String)
    status = Column(String)
    pubg_id = Column(BigInteger)
    login = Column(Integer)
    password = Column(String)
    created_at = Column(DateTime)

    # userStats = relationship('UserStats', back_populates='user', uselist=False)
    orders = relationship('Orders', back_populates='user')

    _name_idx = db.Index('telegram_id', 'status')
