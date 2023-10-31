from sqlalchemy import Column,Boolean, ForeignKey, Integer, String
from database import Base
from sqlalchemy.orm import relationship


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key = True, index= True)
    name= Column(String)
    # age = Column(Integer)
    enrolled = Column(Boolean)
    user_id= Column(Integer, ForeignKey('users.id')) 

    creator = relationship("Users", back_populates="students")

class Users(Base):
    __tablename__ ="users"
    id = Column(Integer, primary_key = True, index= True)
    name= Column(String)
    email = Column(String)
    password = Column(String)

    students = relationship('Student', back_populates="creator")
