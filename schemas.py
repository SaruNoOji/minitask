from pydantic import BaseModel, EmailStr, Field
from pydantic import EmailStr


class UserBase(BaseModel):

    username: str = Field(min_length=3, max_length=30)
    email: EmailStr
    password: str

