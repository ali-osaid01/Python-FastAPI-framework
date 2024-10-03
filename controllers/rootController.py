from models.todoModel import getAllTodos
from fastapi import APIRouter
from utils.helpers import generateResponse

router = APIRouter(prefix="/api", tags=["default"])


@router.get("/")
async def root_api():
    return generateResponse("Health Check Passed")
