from fastapi import APIRouter
from fastapi import Body
from services.user_service import UserService
from models.user_model import UserModel 

router = APIRouter(prefix="/api/auth", tags=["default"])

user_service = UserService()  

@router.post("/register")
async def register(request: UserModel = Body(...)): 
    response = await user_service.register(request)  
    return response


  
