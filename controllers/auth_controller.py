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
        print("API CALLED")
        print(user)
        print("BODYYY",Body)
        # created_user = await user_service.create_user(user)  
        return generateResponse("User registration successful", data=None)

    except HTTPException as http_error:
        raise http_error
    except Exception as e:
        return generateResponse("An error occurred during registration", statusCode=500)
