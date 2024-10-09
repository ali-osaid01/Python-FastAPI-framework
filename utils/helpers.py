from fastapi.responses import JSONResponse
from fastapi import HTTPException

def generateResponse(message: str, data: dict = None, statusCode: int = 200):
    responseContent = {
        "statusCode": statusCode,
        "message": message,
        "data": data
    }
    return JSONResponse(content=responseContent, status_code=statusCode)

def generateErrorResponse(status_code: int, detail: str):
    raise HTTPException(status_code=status_code,detail=detail)