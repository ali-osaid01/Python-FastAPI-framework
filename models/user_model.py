from pydantic import BaseModel, EmailStr
from typing import Optional
from bson import ObjectId

class UserModel(BaseModel):
    email: EmailStr
    password: Optional[str] = None  
    hashed_password: Optional[str] = None  

    class Config:
        orm_mode = True
        json_encoders = {
            ObjectId: str
        }
