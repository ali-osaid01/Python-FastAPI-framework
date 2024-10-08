from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from utils.helpers import generateResponse
from controllers.rootController import router as root_router
from controllers.auth_controller import router as auth_router
from controllers.user_controller import router as user_router
from middleware.auth_middleware import JWTMiddleware
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(JWTMiddleware)

@app.exception_handler(HTTPException)
async def custom_http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail, "statusCode": exc.status_code},
    )

@app.get("/")
def root():
    return generateResponse("Welcome to the Toucher API")

app.include_router(root_router) 
app.include_router(auth_router) 
app.include_router(user_router)