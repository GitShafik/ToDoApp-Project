from abc import ABC, abstractmethod
from typing import List
from domain.task import Task

class TaskRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[Task]:
        pass

    @abstractmethod
    def add(self, task: Task) -> Task:
        pass