from motor.motor_asyncio import AsyncIOMotorCollection

from models import UserCreate, UserInDB  # Import your Pydantic models
from base_repository import BaseRepository  # Import BaseRepository from the same folder

class UserRepository(BaseRepository[UserCreate, UserInDB]):
    def __init__(self, collection: AsyncIOMotorCollection):
        super().__init__(collection)

  