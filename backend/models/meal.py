from sqlalchemy import Column,String,Integer
from backend.db.base import Base


class Meal1(Base):
    __tablename__ = "breakefast"
    
    id = Column(Integer,primary_key=True,index=True)
    day = Column(String)
    name = Column(String)
    category = Column(String)
    calories = Column(Integer)
    description = Column(String)
    image = Column(String)
    

class Meal2(Base):
    __tablename__ = "lunch"
    
    id = Column(Integer,primary_key=True,index=True)
    day = Column(String)
    name = Column(String)
    category = Column(String)
    calories = Column(Integer)
    description = Column(String)
    image = Column(String)


class Meal3(Base):
    __tablename__ = "dinner"

    id = Column(Integer,primary_key=True,index=True)
    day = Column(String)
    name = Column(String)
    category = Column(String)
    calories = Column(Integer)
    description = Column(String)
    image = Column(String)
