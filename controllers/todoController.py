from fastapi import APIRouter, HTTPException
from utils.helpers import generateResponse
from models.todoModel import getAllTodos, createTodo, getTodoById
from models.todoModel import Todo

router = APIRouter(prefix="/api/todo", tags=["todo"])


@router.get("/", summary="Retrieve all todos")
async def fetchAllTodos():
    response = await getAllTodos()
    if response and len(response) > 0:
        return generateResponse("Successfully retrieved todos", response)
    return generateResponse("No todos found", None)


@router.post("/", summary="Create a new todo")
async def addTodo(todo: Todo):
    response = await createTodo(todo.model_dump())  # model_dump() return a dictionary
    if response:
        return response
    raise HTTPException(400, "Failed to create todo")


@router.get("/{id}", summary="Retrieve a todo by id")
async def fetchTodoById(id: str):
    response = await getTodoById(id)
    if response:
        return generateResponse("Successfully retrieved todo", response)
    raise HTTPException(404, "Todo not found")
