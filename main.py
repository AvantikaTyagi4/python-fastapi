from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()   

# @app.get('/')
# def index():
#     return "hello"

# to return JSOn
@app.get('/')
def index():
    return {"data":{"name": "Jack"}}

@app.get('/about')
def about():
    return {'data':'about page'}

# Always place the path variable Url with similar routes above the methods with path variable because fast api is interpreter
@app.get('/blog/unpublished') 
def show_blog():     
    return {'data':"unpublished"}


# to pass path variable
@app.get('/blog/{id}') # to define the type of path variable 
def show_blog(id):     # (id: int)
    return {'data':id}

# query parameters example
@app.get('/students')
def get_students(limit): # limit is query parameter 
    return {"data": f"{limit} students list"}

# muliple query parameters example
@app.get('/students/enrolled')
def get_students(limit, enrolled: bool): # limit, enrolled is query parameter 
    if enrolled:
        return {"data": f"{limit} students enrolled"}
    else:
        return  {"data": f"{limit} students"}
    
# to give default values to the query parameters
# the Url is case sensitive
@app.get('/students/enrolled/class-X')
def get_students(limit = 10, enrolled: bool = True): # limit, enrolled is query parameter 
    if enrolled:
        return {"data": f"{limit} students enrolled in class-X"}
    else:
        return  {"data": f"{limit} students in class-X"}


# Optional queryparamters
# Optional should be imported from typing
@app.get('/students/enrolled/class-X/science')
def get_students(limit = 10, enrolled: bool = True, sort: Optional[str]= None): # limit, enrolled, sort is query parameter 
    if enrolled:
        return {"data": f"{limit} students enrolled in class-X"}
    else:
        return  {"data": f"{limit} students in class-X"}
    
# Request Body Example
# # We need to create Model for Request body
# Base model needs to imported from pydantic
class Student(BaseModel):
    name: str
    age: int
    enrolled: Optional[bool]

@app.post('/save')
def save_student(student: Student):
    # return student
    # to access request body fields
    return f'Student details saved with name {student.name}'
