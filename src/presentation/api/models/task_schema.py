from pydantic import BaseModel

class TaskCreate(BaseModel):
    title: str
    priority: str
    
    
class TaskUpdate(BaseModel):
    title: str
    priority: str