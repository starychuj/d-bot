from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import func
__all__ = ["aMessage","sMessage","zMessage","tMessage","createSession","getRandomMessage"]
Base = declarative_base()
class aMessage(Base):
    __tablename__ = 'adam'
    id = Column(Integer, primary_key=True)
    message = Column(String)
    def __repr__(self):
        return self.message
class sMessage(Base):
    __tablename__ = 'spike'
    id = Column(Integer, primary_key=True)
    message = Column(String)
    def __repr__(self):
        return self.message
class zMessage(Base):
    __tablename__ = 'zawo'
    id = Column(Integer, primary_key=True)
    message = Column(String)
    def __repr__(self):
        return self.message
class tMessage(Base):
    __tablename__ = 'tocha'
    id = Column(Integer, primary_key=True)
    message = Column(String)
    def __repr__(self):
        return self.message
def createSession():
    engine = create_engine('sqlite:///messages.db',echo=False)
    sessioon = sessionmaker(bind=engine)
    return sessioon()
def getRandomMessage(obj,session):
    message = session.query(obj).order_by(func.random()).first()
    session.close()
    return message