from models.user_model import UserModel  
from repository.base_repository import BaseRepository  

class UserRepository(BaseRepository[UserModel, UserModel]):
    def __init__(self):
        print(UserModel)
        super().__init__(UserModel)

  