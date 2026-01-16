from sqlalchemy import or_
from sqlalchemy.orm.session import Session
from db.hash import Hash
from db.models import DbUser
from schemas import UserBase
from fastapi import HTTPException,status

def create_user(db: Session, request: UserBase):

    #handle errors

    new_user = DbUser(

        username = request.username,
        email = request.email,
        password = Hash.bcrypt(request.password)

    )
    exist = db.query(DbUser).filter(
        or_(
            DbUser.username == request.username,
            DbUser.email == request.email
            )
            ).first()
    if exist:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Username or email already exists")
    

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_all_users(db:Session):

    return db.query(DbUser).all()

def get_user(db:Session,id:int):

    user = db.query(DbUser).filter(DbUser.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="user not found")
    #handle error

    return user

def delete_user(db:Session, id:int):

    user = db.query(DbUser).filter(DbUser.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="user not found")

    db.delete(user)
    db.commit()

    return status.HTTP_204_NO_CONTENT