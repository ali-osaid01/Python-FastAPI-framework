from motor.motor_asyncio import AsyncIOMotorCollection

from models.user_model import UserModel  
from repository.base_repository import BaseRepository  

class UserRepository(BaseRepository[UserModel, UserModel]):
    def __init__(self, collection: AsyncIOMotorCollection):
        super().__init__(collection)

  