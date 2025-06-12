from abc import ABC, abstractmethod
from typing import List
from domain.task import Task

class TaskRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[Task]:
        pass
    
    @abstractmethod
    def get_by_id(self, task_id: int) -> Task:
        pass

    @abstractmethod
    def add(self, task: Task) -> Task:
        pass
    
    @abstractmethod
    def update(self, task: Task) -> Task:
        pass

    @abstractmethod
    def delete(self, task: Task) -> Task:
        pass
    
    @abstractmethod
    def mark_complete(self, task_id: int) -> Task:
        pass