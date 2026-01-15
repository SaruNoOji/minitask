from typing import List
from webbrowser import get
from fastapi import APIRouter, Depends
from fastapi import status
from schemas import UserBase, DisplayUser
from sqlalchemy.orm.session import Session
from db.database import get_db
from db import users_database

router = APIRouter(
    prefix='/users',
    tags=['users']
)

@router.get("/",status_code=status.HTTP_200_OK ,response_model=List[DisplayUser])
def get_all_users(db: Session = Depends(get_db)):
    return users_database.get_all_users(db)

@router.post("/", status_code=status.HTTP_200_OK, response_model=DisplayUser)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return users_database.create_user(db,request)

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=DisplayUser)
def get_user(id:int,db:Session=Depends(get_db)):
    return users_database.get_user(db,id)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_user(id:int, db:Session =Depends(get_db)):
    return users_database.delete_user(db,id)