from typing import List
from rich.console import Console
from rich.panel import Panel
from application.service import TaskService
from domain.task import Task


class TaskCLIRich:
    def __init__(self, service: TaskService):
        self.service = service
        self.console = Console()

    def run(self):
        while True:
            self._display_menu()

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

    def _display_menu(self):

        menu = Panel("""
            [bold cyan]1.[/] Lägg till uppgift
            [bold cyan]2.[/] Lista uppgifter
            [bold cyan]3.[/] Markera uppgift som klar
            [bold cyan]4.[/] Ta bort uppgift
            [bold cyan]5.[/] Avsluta
        """, title="[bold]Todo List App[/]", border_style="cyan")
        self.console.print(menu)
