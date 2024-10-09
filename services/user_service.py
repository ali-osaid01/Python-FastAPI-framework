from repository.user_repository import UserRepository  
from models.user_model import UserModel  
from utils.helpers import generateErrorResponse,generateResponse
from utils.jwt_handler import create_access_token
from models.helper_model import APIResponse
from utils.constant import SUCCESS_DATA_INSERTION_PASSED,ERROR_CONFLICT,SUCCESS_LOGIN_PASSED,ERROR_LOGIN

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
    
    async def login(self, user: UserModel) -> APIResponse:
        isUserExist:UserModel = await self.user_repository.get_one({"email": user.email})

        if not isUserExist:
            return generateErrorResponse(400, ERROR_LOGIN)

        if isUserExist["password"] == user.password:
            token = create_access_token(isUserExist)
            return generateResponse(SUCCESS_LOGIN_PASSED, {"user": isUserExist, "accessToken": token}, 200)

        return generateErrorResponse(400, ERROR_LOGIN)

        
    async def get_users(self) -> APIResponse: 
        users = await self.user_repository.get_all()
        return generateResponse("SUCCESS_DATA_LIST_PASSED",users,200)
   
