from os import read
from sqlalchemy.orm.session import Session
from db.models import DbTasks, DbUser
from schemas import TasksCreate, TaskUpdate
from fastapi import HTTPException, status

def create_task(db: Session, request: TasksCreate, user_id: int):

    #handle errors
    user = db.query(DbUser).filter(DbUser.id == user_id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')

    new_task = DbTasks(

        title = request.title,
        description = request.description,
        status = request.status,
        user_id = user_id

    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

def get_task(db:Session,id:int):
    
    task = db.query(DbTasks).filter(DbTasks.id == id).first()

    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "Task not found")
    
    return task


def update_task(db: Session, request: TaskUpdate, id:int):

    task = db.query(DbTasks).filter(DbTasks.id == id).first()

    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "Task not found")
    
    if request.title is not None:
        task.title = request.title
    if request.description is not None:
        task.description = request.description
    if request.status is not None:
        task.status = request.status

    db.commit()

    return task
