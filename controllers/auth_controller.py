from fastapi import APIRouter, HTTPException
from fastapi import Body
from utils.helpers import generateResponse
from services.user_service import UserService
from models.user_model import UserModel 

router = APIRouter(prefix="/api/auth", tags=["default"])

user_service = UserService()  

@router.post("/register")
async def register(request: UserModel = Body(...)): 
    response = await user_service.create_user(request)  
    return response

  
