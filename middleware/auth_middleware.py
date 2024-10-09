from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse
from fastapi import HTTPException, Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from utils.jwt_handler import verify_token

security = HTTPBearer()

class JWTMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        excluded_paths = ["/api/auth/register", "/api/auth/login",'/api/','/']
        print(request.url.path)
        if request.url.path in excluded_paths:
                    return await call_next(request)
        try:

         
            credentials: HTTPAuthorizationCredentials = await security(request)
            token = credentials.credentials

            payload = verify_token(token)

            if payload is None:
                raise HTTPException(status_code=401, detail="Invalid or expired token")

            response = await call_next(request)
            return response

        except HTTPException as e:
            return JSONResponse(
                status_code=e.status_code,
                content={"detail": e.detail}
            )

        except Exception as e:
            return JSONResponse(
                status_code=500,
                content={"detail": "Internal server error"}
            )
