class Task:
    def __init__(self, task_id: int, title: str, priority: str = "Medium", completed: bool = False):
        self.id = task_id
        self.title = title
        self.priority = priority
        self.completed = completed