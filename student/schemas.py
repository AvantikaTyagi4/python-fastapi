from pydantic import BaseModel
from typing import Optional, List

class StudentModel(BaseModel):

    name: str
    enrolled: Optional[bool]
    class Config():
        orm_mode = True

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
    students: List[StudentModel] =[]
    class Config():
        from_attributes = True


# config() is used for exact mapping of SQL model to this model
class ShowStudent(StudentModel):
    creator: ShowUser
    class Config():
        orm_mode = True
    

