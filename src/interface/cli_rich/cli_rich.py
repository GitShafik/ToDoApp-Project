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

            if ch == "8":
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
                
                case "3":
                    task_id = int(input(" Ange ID för uppgiften som ska markeras klar: "))
                    self.service.mark_complete(task_id)
                    
                case "4":
                    task_id = int(input("Ange uppgiftens ID för att avmarkera: "))
                    self.service.unmark_complete(task_id)
                    
                case "5":
                    pass
                
                case "6":
                    pass
                
                case "7":
                    task_id = int(input("ID: "))
                    task = self.service.get_task_by_id(task_id=task_id)
                    self._list_tasks([task])
                    

    @staticmethod
    def _list_tasks(tasks: List[Task]) -> None:
        for task in tasks:
            status = "✓" if task.completed else " "
            print(f"- [{status}] ID: {task.id} - {task.title} : {task.priority}")

    def _display_menu(self):

        menu = Panel("""
            [bold cyan]1.[/] Lägg till en ny uppgift
            [bold cyan]2.[/] Lista alla uppgifter
            [bold cyan]3.[/] Markera uppgift som klar
            [bold cyan]4.[/] Avmarkera uppgift
            [bold cyan]5.[/] Ta bort uppgift
            [bold cyan]6.[/] Uppdatera en uppgift
            [bold cyan]7.[/] Visa en uppgift med ID
            [bold cyan]8.[/] Avsluta programmet
        """, title="[bold]Todo List App[/]", border_style="cyan")
        self.console.print(menu)
