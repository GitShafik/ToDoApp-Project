from typing import List
from application.interfaces import TaskRepository
from domain.task import Task

class InMemoryTaskDB(TaskRepository):
    def __init__(self):
        self.tasks = []
        self.max_id = 0

    def _get_next_id(self):
        pass

    def get_all(self) -> List[Task]:
        return self.tasks

    def add(self, task: Task) -> Task:
        task_id = len(self.tasks) + 1
        task.id = task_id
        self.tasks.append(task)
        return task