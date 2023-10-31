from pydantic import BaseModel
from typing import Optional

class StudentModel(BaseModel):

    name: str
    enrolled: Optional[bool]

# config() is used for exact mapping of SQL model to this model
class ShowStudent(StudentModel):
    class Config():
        orm_mode = True


class Users(BaseModel):
    name: str
    email:str
    password: str

class ShowUser(BaseModel):
    name: str
    email:str

    class Config():
        from_attributes = True
    

