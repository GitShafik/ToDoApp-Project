from fastapi import APIRouter
from presentation.api.service_manager import ServiceManager
from presentation.api.models.task_schema import TaskCreate, TaskUpdate


router = APIRouter(prefix="/api/tasks")

@router.get("")
def get_tasks():
    
    service = ServiceManager.get_service()
    tasks = service.get_all_tasks()
    return tasks

@router.get("/{task_id}")
def get_task(task_id: int):
    service = ServiceManager.get_service()
    task = service.get_task_by_id(task_id)
    return task

@router.post("")
def create_task(task: TaskCreate):
    service = ServiceManager.get_service()
    new_task = service.create_task(title= task.title, priority= task.priority)
    return new_task

@router.put("/{task_id}")
def update_task(task_id: int, updated_task: TaskUpdate):
    service = ServiceManager.get_service()
    task = service.update_task(updated_task.title, task_id, updated_task.priority)
    return task
