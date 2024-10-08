from motor.motor_asyncio import AsyncIOMotorCollection

from models import UserModel  
from base_repository import BaseRepository  

class UserRepository(BaseRepository[UserModel, UserModel]):
    def __init__(self, collection: AsyncIOMotorCollection):
        super().__init__(collection)

  