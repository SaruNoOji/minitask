from fastapi import APIRouter, Depends, status
from sqlalchemy.orm.session import Session
from db.database import get_db
from db import tasks_database
from schemas import TasksDisplay, TaskUpdate

router = APIRouter(
    prefix='/tasks',
    tags=['tasks']
)


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=TasksDisplay)
def get_task(id:int, db: Session = Depends(get_db)):
    return tasks_database.get_task(db,id)

@router.patch("/{id}",status_code=status.HTTP_200_OK, response_model=TasksDisplay)
def update_task(id: int, request : TaskUpdate ,db: Session = Depends(get_db)):
    return tasks_database.update_task(db,request,id)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(id:int, db:Session = Depends(get_db)):
    return tasks_database.delete_task(db,id)