from pydantic import BaseModel, EmailStr, Field
from pydantic import EmailStr


class UserBase(BaseModel):

    username: str = Field(min_length=3, max_length=30)
    email: EmailStr
    password: str

class DisplayUser(BaseModel):

    id: int
    username : str
    email: str