# MongoDB driver
from motor.motor_asyncio import AsyncIOMotorClient

# Connect to MongoDB
client = AsyncIOMotorClient("mongodb://127.0.0.1:27017")
if client:
    print("Connected to MongoDB")

# Database
database = client.TodoList
