from fastapi import APIRouter
from utils.helpers import generateResponse

router = APIRouter(prefix="/api/user", tags=["default"])


@router.get("/")
async def users():
    return generateResponse("Health Check Passed")
