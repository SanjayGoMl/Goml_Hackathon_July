from fastapi import APIRouter, HTTPException
from models.todos import Todo
from config.database import collection_name
from schema.schemas import list_serial
from bson import ObjectId

router = APIRouter()

#Get Request Method
@router.get("/")
async def get_todos():
    todos = list_serial(collection_name.find())
    return todos

#POST Request Method
@router.post("/")
async def post_todo(todo: Todo):
    collection_name.insert_one(dict(todo))
    
@router.delete("/")
async def delete_all_todos():
    result = collection_name.delete_many({})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="No todos found to delete")
    return {"message": f"Deleted {result.deleted_count} todos"}
