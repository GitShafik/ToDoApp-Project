from typing import List

from application.interfaces import TaskRepository
from domain.task import Task
from infrastructure.sqlite.sqlite_database import SQLiteDatabase

class SQLiteTaskRepo(TaskRepository):
    
    def __init__(self, db: SQLiteDatabase):
        self.db = db
    
    def get_all(self) -> List[Task]:
        query = "SELECT id, title, priority, completed FROM tasks"
        rows = self.db.execute_many(query)
        return [Task
                (task_id=row[0], title=row[1], priority=row[2], completed= bool(row[3]))
                for row in rows
        ]
        
    def get_by_id(self, task_id:int) -> Task:
        query = "SELECT id, title, priority, completed FROM tasks WHERE id = ?"
        row = self.db.execute_one(query, (task_id,))
        if not row:
            raise ValueError(f"Task with id{task_id} not found ")
        return Task(task_id=row[0], title=row[1], priority=row[2], completed=bool (row[3]))
        
        
    def add(self, task: Task) -> Task:
        query = "INSERT INTO tasks (title, priority) VALUES (?, ?)"
        task_id = self.db.insert(query, (task.title, task.priority))
        task.id = task_id
        return task
    
    def update(self, task: Task) -> Task:
        query = "UPDATE tasks SET title = ?, priority = ?, completed = ?, WHERE id = ? "
        task = self.db.execute(query, (task.title, task. priority, task.completed, task.id))
        return task
    
    def delete(self, task_id: int) -> Task:
        query = "DELETE FROM tasks WHERE id = ?"
        self.db.execute(query,(task_id))
        
    def mark_complete(self, task_id: int) -> Task:
        query = "UPDATE tasks SET complete = ? where id = ?"
        params = (1, task_id)
        self.db.execute(query, params)
        