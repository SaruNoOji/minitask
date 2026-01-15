from fastapi import FastAPI
from routers import Users
from routers import Tasks
from db.database import engine
from db import models

app = FastAPI()

app.include_router(Users.router)
app.include_router(Tasks.router)

models.Base.metadata.create_all(engine)

@app.get("/")
def index():
    return{"message":"start page"}
