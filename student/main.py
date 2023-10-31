
from typing import List
from fastapi import FastAPI, Depends, status,Response, HTTPException
import schemas,models
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from hashing import Hash

app = FastAPI()

models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# @app.post('/student', status_code= 201, tags=['students'])
# tags is used to grouping the apis in tags in swagger
@app.post('/student',status_code= status.HTTP_201_CREATED,  tags=['students'])
def create(student: schemas.StudentModel, db: Session = Depends(get_db)):
    new_student = models.Student( name = student.name, enrolled = student.enrolled, user_id = 1)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student
    

# @app.get("/student")
# def all(db: Session = Depends(get_db)):
#     students = db.query(models.Student).all()
#     return students

# to get student by id if id not exist return null
# @app.get('/student/{id}')
# def show(id, db: Session = Depends(get_db)):
#     student = db.query(models.Student).filter(models.Student.id == id).first()
#     return student

# to provide custom status code and message if id not exist it gives proper message with status code
# @app.get('/student/{id}', status_code= 200)
# def show(id, response: Response, db: Session = Depends(get_db)):
#     student = db.query(models.Student).filter(models.Student.id == id).first()
#     if not student:
#         response.status_code = status.HTTP_404_NOT_FOUND
#         return {"detail":f'Student with {id} not found'}
#     else:
#         return student

# to throw exception if id not exist
# @app.get('/student/{id}', status_code= 200)
# def show(id, response: Response, db: Session = Depends(get_db)):
#     student = db.query(models.Student).filter(models.Student.id == id).first()
#     if not student:
#         raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail =f'Student with {id} not found')
#     else:
#         return student
    

@app.delete('/student/{id}', status_code=status.HTTP_204_NO_CONTENT,  tags=['students'])
def delete(id, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.id == id).delete(synchronize_session= False)
    db.commit()
    return 'deleted'

@app.put('/student/{id}', status_code= status.HTTP_202_ACCEPTED , tags=['students'])
def update(id, student: schemas.StudentModel, db: Session = Depends(get_db)):
    student= db.query(models.Student).filter(models.Student.id == id)
    if not student.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Student with {id} not found')
    student.update({'name': student.name,'enrolled':student.enrolled})
    db.commit()
    return 'updated'

# to use response model map sql model to pydantic model
@app.get('/student/{id}', status_code= 200, response_model=schemas. ShowStudent , tags=['students'])
def show(id, response: Response, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.id == id).first()
    if not student:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail =f'Student with {id} not found')
    else:
        return student
    
@app.get("/student", response_model= List[schemas.ShowStudent] , tags=['students'])
def all(db: Session = Depends(get_db)):
    students = db.query(models.Student).all()
    return students

# to encrpt password
# pwd_cxt = CryptContext(schemes=["bcrypt"],deprecated ='auto')

# # user
# @app.post('/user')
# def create_user(user: schemas.Users, db: Session = Depends(get_db)):
#     hashedPassword = pwd_cxt.hash(user.password)
#     new_user = models.Users(name = user.name, email = user.email, password= hashedPassword)
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user

#  another way of doing same by keeping the encyption code in seperate file
@app.post('/user', response_model= schemas.ShowUser, tags=['users'])
def create_user(user: schemas.Users, db: Session = Depends(get_db)):
    
    new_user = models.Users(name = user.name, email = user.email, password=Hash.bcrypt(user.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.get('/user/{id}',  status_code= status.HTTP_200_OK, response_model=schemas.ShowUser , tags=['users'])
def get_user_by_id(id, response:Response, db:Session = Depends(get_db)):
    user = db.query(models.Users).filter(models.Users.id == id).first()
    if not user:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"No user found with id {id}.")
    else:
        return user
    
@app.get('/users/all', status_code= 200, response_model= List[schemas.ShowUser], tags=['users'])
def get_all_users(db: Session = Depends(get_db)):
    students = db.query(models.Users).all()
    return students