# MongoDB driver
from motor.motor_asyncio import AsyncIOMotorClient

# Connect to MongoDB
client = AsyncIOMotorClient("mongodb+srv://aliusaid55:y0OTidCWrGVegbAJ@cluster0.88l9ne8.mongodb.net/python-fast-api")
if client:
    print("Connected to MongoDB")

# Database
database = client["python-fast-api"]

