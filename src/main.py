from application.service import TaskService
from interface.cli_rich.cli_rich import TaskCLIRich
from infrastructure.inmemory.inmemory import InMemoryTaskDB
from infrastructure.sqlite.sqlite_database import SQLiteDatabase
from infrastructure.sqlite.sqlite_tasks_repo import SQLiteTaskRepo


def main():
    db = SQLiteDatabase()
    repo = SQLiteTaskRepo(db)
    
    service = TaskService(repo)
    
 
    cli = TaskCLIRich(service)

    cli.run()

if __name__ == '__main__':
    main()