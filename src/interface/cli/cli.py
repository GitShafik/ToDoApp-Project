from typing import List
from application.service import TaskService
from domain.task import Task

class TaskCLI:
    def __init__(self, service: TaskService):
        self.service = service

    def run(self):
        while True:
            print("\n=== ToDo App ===")
            print("1. Lägg till ny uppgift")
            print("2. Lista alla uppgifter")
            print("3. Visa en uppgift med ID")
            print("4. Markera uppgift som färdig")
            print("4. Avmarkera uppgift")
            
            print("5. Avsluta")

            ch = input("Välj ett alternativ (1-5): ")

            if ch == "5":
                print("Avslutar...")
                break

            match ch:
                case "1":
                    title = input("Ange uppgiftens titel: ")
                    print("1. Låg, 2. Medium, 3. Hög")
                    prio_in = input("Ange prioritet för uppgiften: ")
                    prio = {
                        "1": "Låg",
                        "2": "Medium",
                        "3": "Hög"
                    }.get(prio_in, "Medium")


                    self.service.create_task(title=title, priority=prio)
                case "2":
                    tasks = self.service.get_all_tasks()
                    self._list_tasks(tasks)
            """case "3":
                    list_tasks()
                    task_id = input("ID: ")
                    app.mark_completed(task_id)"""

    @staticmethod
    def _list_tasks(tasks: List[Task]) -> None:
        for task in tasks:
            status = "✓" if task.completed else " "
            print(f"- [{status}] ID: {task.id} - {task.title} : {task.priority}")