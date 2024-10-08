from fastapi import APIRouter, HTTPException
from fastapi import Body
from utils.helpers import generateResponse
from services.user_service import UserService
from models.user_model import UserModel 

router = APIRouter(prefix="/api/auth", tags=["default"])

user_service = UserService()  

@router.post("/register")
async def register(user: UserModel = Body(...)): 
    try:
        created_user = await user_service.create_user(user)  
        return generateResponse("User registration successful", data=created_user)

    except Exception as e:
        print(e)
        return generateResponse("An error occurred during registration", statusCode=500)
