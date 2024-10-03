from fastapi.responses import JSONResponse


def generateResponse(message: str, data: dict = None, statusCode: int = 200):
    responseContent = {
        "statusCode": statusCode,
        "message": message,
        "data": data
    }
    return JSONResponse(content=responseContent, status_code=statusCode)