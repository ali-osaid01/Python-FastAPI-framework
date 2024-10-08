from pydantic import BaseModel, EmailStr
from typing import Optional
from bson import ObjectId

class UserModel(BaseModel):
    email: EmailStr
    password: Optional[str] = None  

    class Config:
        from_attributes = True
        json_encoders = {
            ObjectId: str
        }
