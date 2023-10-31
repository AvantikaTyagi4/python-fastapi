from sqlalchemy import Column,Boolean, Integer, String
from database import Base


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key = True, index= True)
    name= Column(String)
    # age = Column(Integer)
    enrolled = Column(Boolean)

class Users(Base):
    __tablename__ ="users"
    id = Column(Integer, primary_key = True, index= True)
    name= Column(String)
    email = Column(String)
    password = Column(String)