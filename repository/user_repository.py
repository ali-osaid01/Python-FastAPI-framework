from models.user_model import UserModel
from repository.base_repository import BaseRepository
from config.dbConfig import database

class UserRepository(BaseRepository[UserModel, UserModel]):
    def __init__(self):
        super().__init__(database['users'])
        print("USERMODEL", UserModel)

