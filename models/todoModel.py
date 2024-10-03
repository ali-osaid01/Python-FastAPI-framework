from pydantic import BaseModel
from config.dbConfig import database
from bson import ObjectId


class Todo(BaseModel):
    title: str
    description: str


collection = database.todo


def str_to_objectid(id):
    try:
        return ObjectId(id)
    except Exception:
        raise ValueError("Invalid ObjectId")

async def getAllTodos():
    cursor = collection.find({})
    todos = await cursor.to_list(length=None) 
    
    # Convert ObjectId to string for each document.
    for document in todos:
        document["_id"] = str(document["_id"])  # Convert ObjectId to string for JSON serialization.

    return todos

async def getTodoById(id):
    id = str_to_objectid(id) 
    todo = await collection.find_one({"_id": id})
    if todo:
        todo["_id"] = str(todo["_id"])
        return todo
    return None


async def createTodo(todo):
    result = await collection.insert_one(todo)
    todo["_id"] = str(result.inserted_id)
    return todo
