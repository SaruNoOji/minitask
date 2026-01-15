from pickletools import read_uint1
from sqlalchemy.orm.session import Session
from db.hash import Hash
from db.models import DbUser
from schemas import UserBase

def create_user(db: Session, request: UserBase):

    #handle errors

    new_user = DbUser(

        username = request.username,
        email = request.email,
        password = Hash.bcrypt(request.password)

    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_all_users(db:Session):

    return db.query(DbUser).all()

def get_user(db:Session,id:int):

    user = db.query(DbUser).filter(DbUser.id == id).first()
    #handle error

    return user