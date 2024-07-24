from pydantic import BaseModel

class Todo(BaseModel):
    query:str
    response: str 
    complete: bool 