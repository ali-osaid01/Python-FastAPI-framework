# user_service.py

from repository.user_repository import UserRepository  # Import UserRepository
from models import UserModel  # Assuming UserModel is your Pydantic model
from fastapi import HTTPException

class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def create_user(self, user: UserModel) -> UserModel:
        
        existing_user = await self.user_repository.get_one({"email": user.email})
        if existing_user:
            raise HTTPException(status_code=400, detail="Email already registered")
        
        created_user = await self.user_repository.create(user)
        return created_user

   
   
