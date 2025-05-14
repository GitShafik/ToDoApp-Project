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