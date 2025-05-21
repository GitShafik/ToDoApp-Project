from typing import List
from application.interfaces import TaskRepository
from domain.task import Task

class TaskService:
    def __init__(self, task_repository: TaskRepository):
        self.task_repository = task_repository

    def create_task(self, title: str, priority: str) -> Task:
        task = Task(task_id=0, title=title, priority=priority)
        self.task_repository.add(task)
        return task

    def get_all_tasks(self) -> List[Task]:
        return self.task_repository.get_all()
    
    def update_task(self, title: str, task_id: int, priority: str) -> Task:
        task = self.task_repository.get_by_id(task_id)
        task.title = title
        task.priority = priority
        return self.task_repository.update(task)
    
    def get_task_by_id(self, task_id: int) -> Task:
        return self.task_repository.get_by_id(task_id)
    
    def mark_complete(self, task_id: int,) -> Task:
       task =  self.task_repository.get_by_id(task_id)
       task.completed = True
       return self.task_repository.update(task)
   
    def unmark_complete(self, task_id: int) -> Task:
        task = self.task_repository.get_by_id(task_id)
        task.completed = False
        return self.task_repository.update(task)