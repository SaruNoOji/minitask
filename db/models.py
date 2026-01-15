from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import String, Integer, DateTime
from db.database import Base
from sqlalchemy import Column
from sqlalchemy.orm import relationship

class DbUser(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True )
    username = Column(String, unique=True)
    email = Column (String,unique=True)
    password = Column(String)