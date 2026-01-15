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

@router.get("/")
def index():
    return "Ok"

@router.post("/", status_code=status.HTTP_200_OK, response_model=DisplayUser)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return users_database.create_user(db,request)