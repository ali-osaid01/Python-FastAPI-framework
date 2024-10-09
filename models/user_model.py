from pydantic import BaseModel, EmailStr, constr
from typing import Optional
from bson import ObjectId

class UserModel(BaseModel):
    id: Optional[str] = None
    email: EmailStr
    password: Optional[str] = None
    fcmToken: Optional[str] = None  
    refreshToken: Optional[str] = None  
    phone: Optional[str] = None  

    class Config:
        from_attributes = True
        json_encoders = {
            ObjectId: str
        }
        
        
