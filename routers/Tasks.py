from fastapi import APIRouter

router = APIRouter(
    prefix='/tasks',
    tags=['tasks']
)

@router.get("/")
def index():
    return "Ok"