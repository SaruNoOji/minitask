from fastapi import FastAPI
from routers import Users
from routers import Tasks

app = FastAPI()

app.include_router(Users.router)
app.include_router(Tasks.router)

@app.get("/")
def index():
    return{"message":"start page"}
