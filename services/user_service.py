from repository.user_repository import UserRepository  
from models.user_model import UserModel  
from utils.helpers import generateErrorResponse

class UserService:
    def __init__(self):
        self.user_repository = UserRepository

    async def create_user(self, user: UserModel) -> UserModel:
        
        existing_user: UserModel = await self.user_repository.get_one({"email": user.email}) 
        if existing_user:
            generateErrorResponse(400, "User already Exist")
        
        created_user = await self.user_repository.create(user)
        return created_user

   
   
