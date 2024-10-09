from fastapi.responses import JSONResponse
from typing import Any, Dict
from fastapi import HTTPException

def generateResponse(message: str, data: Dict[str, Any] = None, statusCode: int = 200) -> JSONResponse:
    responseContent = {
        "message": message,
        "data": data
    }
    return JSONResponse(content=responseContent, status_code=statusCode)



def generateErrorResponse(status_code: int, detail: str):
    raise HTTPException(status_code=status_code,detail=detail)