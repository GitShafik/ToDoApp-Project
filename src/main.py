import os
from dotenv import load_dotenv

from application.services import TaskService
"""
from infrastructure.sqlite.sqlite_database import SQLiteDatabase
from infrastructure.sqlite.sqlite_tasks_repo import SQLiteTaskRepository
from presentation.cli.cli import TaskCLI
from presentation.qtdesktop.qtdesktop import TaskQtDesktop
"""

def main():
    load_dotenv(override=True)

    print("UI selected:", os.getenv("UI"))

    db_type = os.getenv("DBTYPE", "memory")
    ui_type = os.getenv("UI", "cli")
    
    match db_type:
        case "postgres":
            pass
        case "sqlite":
            from infrastructure.sqlite.sqlite_database import SQLiteDatabase
            from infrastructure.sqlite.sqlite_tasks_repo import SQLiteTaskRepository
            db = SQLiteDatabase()
            repo = SQLiteTaskRepository(db)
        case "memory" | _:
            from src.infrastructure.inmemory import InMemoryTaskDB
            repo = InMemoryTaskDB()
            
    service = TaskService(repo)
     
    match ui_type:
        case "qt":
            from presentation.qtdesktop.qtdesktop import TaskQtDesktop
            # Qt desktop presentation
            qt_desktop = TaskQtDesktop(service)
            qt_desktop.run()
            
        case "web":
            from presentation.django.django_app import TaskDjango
            django_app = TaskDjango(service)
            django_app.run()
        case "api":
            from presentation.api.api import API
            api = API(service)
            api.run()
        case "cli":
            from presentation.cli.cli import TaskCLI
            cli = TaskCLI(service)
            cli.run()       
    
    # db = SQLiteDatabase()
    # repo = SQLiteTaskRepository(db)

    # repo = InMemmoryTaskDB()
    # service = TaskService(repo)
    


    # Qt Desktop presentation
    # qt_desktop = TaskQtDesktop(service)
    # qt_desktop.run()

if __name__ == '__main__':
    main()
