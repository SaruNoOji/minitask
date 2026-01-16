from datetime import datetime
from pydantic import BaseModel, EmailStr, Field
from pydantic import EmailStr, ConfigDict
from enum import Enum
from typing import Optional

class TaskStatus(str, Enum):
    new = "new"
    in_progress = "in_progress"
    done = "done"

class UserBase(BaseModel):

    username: str = Field(min_length=3, max_length=30)
    email: EmailStr
    password: str

class DisplayUser(BaseModel):

    id: int
    username : str
    email: str
    model_config = ConfigDict(from_attributes=True)

class TasksCreate(BaseModel):

    title : str = Field(min_length=3,max_length=120)
    description : Optional[str] = Field(None,max_length=1000)
    status : TaskStatus = TaskStatus.new

class TasksDisplay(BaseModel):

    id: int
    title: str
    description : Optional[str]
    status: TaskStatus
    user_id : int
    created_at : datetime
    updated_at : datetime

    model_config = ConfigDict(from_attributes=True)

class TaskUpdate(BaseModel):

    title: Optional[str] = Field(default=None,min_length=3,max_length=120)
    description : Optional[str] = Field(default=None,max_length=1000)
    status : Optional[TaskStatus] = None