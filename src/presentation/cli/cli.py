from typing import List

from application.services import TaskService
from domain.task import Task


class TaskCLI:
    def __init__(self, service: TaskService):
        self.service = service

    def run(self):
        while True:
            print("\n=== Todo List App ===")
            print("1. Lägg till uppgift")
            print("2. Lista uppgifter")
            print("3. Markera uppgift som klar")
            print("4. Ta bort uppgift")
            print("5. Avsluta")

            choice = input("\nVälj ett alternativ (1-5): ")

            try:
                if choice == "1":
                    self._handle_add_task()
                elif choice == "2":
                    self._handle_list_tasks()
                elif choice == "3":
                    self.service.mark_completed(int(input("ID: ")))
                elif choice == "4":
                    pass
                    #self._handle_delete_task()
                elif choice == "5":
                    print("Avslutar programmet...")
                    break
                else:
                    print("Ogiltigt val, försök igen!")
            except Exception as e:
                print(f"Ett fel uppstod: {str(e)}")

    def _handle_add_task(self):
        title = input("Ange uppgiftens titel: ")
        print("\nVälj prioritet:")
        print("1. Låg")
        print("2. Medium")
        print("3. Hög")
        priority_choice = input("Välj prioritet (1-3): ")

        priority_map = {"1": "low", "2": "medium", "3": "high"}
        priority = priority_map.get(priority_choice, "medium")

        self.service.create_task(title=title, priority=priority)
        print("Uppgift tillagd!")

    def _handle_list_tasks(self) -> None:
        tasks = self.service.get_all_tasks()
        self._list_all_tasks(tasks)

    @staticmethod
    def _list_all_tasks(tasks: List[Task]) -> None:
        for task in tasks:
            status = "✓" if task.completed else " "
            print(f"- [{status}] {task.id}. {task.title} [{task.priority}]")