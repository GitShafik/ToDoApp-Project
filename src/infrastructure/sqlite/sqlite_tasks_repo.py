from typing import List

from application.interfaces import TaskRepository
from domain.task import Task
from infrastructure.sqlite.sqlite_database import SQLiteDatabase


class SQLiteTaskRepository(TaskRepository):
    def __init__(self, database: SQLiteDatabase):
        self.database = database

    def add(self, task: Task) -> Task:
        query = "INSERT INTO tasks (title, priority, completed) VALUES (?, ?, ?)"
        task_id = self.database.insert(query, (task.title, task.priority, task.completed))
        task.id = task_id
        return task

    def get_all(self) -> List[Task]:
        query = "SELECT id, title, priority, completed FROM tasks"
        rows = self.database.execute(query)
        return [Task(task_id=row[0], title=row[1], priority=row[2], completed=bool(row[3]))
                for row in rows]

    def get_by_id(self, task_id: int) -> Task:
        query = "SELECT id, title, priority, completed FROM tasks WHERE id = ?"
        row = self.database.execute_one(query, (task_id,))
        if not row:
            raise ValueError(f"Task with id {task_id} not found")
        return Task(task_id=row[0], title=row[1], priority=row[2], completed=bool(row[3]))

    def update(self, task: Task) -> Task:
        query = """
            UPDATE tasks 
            SET title = ?, priority = ?, completed = ?
            WHERE id = ?
        """
        self.database.execute(query, (task.title, task.priority, task.completed, task.id))
        return task

    def mark_complete(self, task_id: int) -> None:
        query = "UPDATE tasks SET completed = 1 WHERE id = ?"
        self.database.execute(query, (task_id,))

    def delete(self, task_id: int) -> None:
        query = "DELETE FROM tasks WHERE id = ?"
        self.database.execute(query, (task_id,))