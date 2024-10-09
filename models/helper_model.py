from pydantic import BaseModel
from typing import Any, Optional

class APIResponse(BaseModel):
    data: Optional[Any]  
    message:str
    status_code: int

    class Config:
        from_attributes = True  
