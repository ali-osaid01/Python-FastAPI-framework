from repository.user_repository import UserRepository  
from models.user_model import UserModel  
from utils.helpers import generateErrorResponse,generateResponse
from utils.jwt_handler import create_access_token
from models.helper_model import APIResponse
from utils.constant import SUCCESS_DATA_INSERTION_PASSED,ERROR_CONFLICT,SUCCESS_DATA_LIST_PASSED
class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    async def register(self, user: UserModel) -> APIResponse:
        existing_user: UserModel = await self.user_repository.get_one({"email":user.email}) 
        if existing_user:
          return generateErrorResponse(400, ERROR_CONFLICT)
        created_user = await self.user_repository.create(user)
        token = create_access_token(created_user)
        return generateResponse(SUCCESS_DATA_INSERTION_PASSED,{"user": created_user, "token": token}, 200)

    async def get_users(self) -> APIResponse: 
        users = await self.user_repository.get_all()
        return generateResponse("SUCCESS_DATA_LIST_PASSED",users,200)
   
