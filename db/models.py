from datetime import datetime, timezone
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import String, Integer, DateTime
from db.database import Base
from sqlalchemy import Column
from sqlalchemy.orm import relationship

class DbUser(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    email = Column (String,unique=True)
    password = Column(String)

    tasks = relationship(
        "DbTasks",
        back_populates="user",
        cascade="all, delete-orphan"
    )


class DbTasks(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, index=True )
    title = Column(String)
    description = Column (String,nullable=True)
    status = Column(String, nullable = False)
    user_id = Column(Integer, ForeignKey('users.id', ondelete="CASCADE"), nullable= False)
    created_at = Column(DateTime, nullable= False, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime, nullable= False, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    user = relationship("DbUser", back_populates="tasks")