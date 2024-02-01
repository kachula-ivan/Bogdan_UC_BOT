from sqlalchemy import Column, Integer, Boolean, String

from database.app import db


class Variables(db.Model):
    __tablename__ = 'variables'

    id = Column(Integer, primary_key=True)
    active = Column(Boolean)
    admin = Column(String)
    manager = Column(String)
    chat_id = Column(Integer)
