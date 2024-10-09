from repository.user_repository import UserRepository  
from models.user_model import UserModel  
from utils.helpers import generateErrorResponse,generateResponse
from utils.jwt_handler import create_access_token
from models.helper_model import APIResponse
class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    async def create_user(self, user: UserModel) -> APIResponse:
        existing_user: UserModel = await self.user_repository.get_one({"email":user.email}) 
        if existing_user:
          return generateErrorResponse(400, "User already Exist")
        created_user = await self.user_repository.create(user)
        token = create_access_token(created_user)
        return generateResponse("User created",{"user": created_user, "token": token}, 200)

   
   
