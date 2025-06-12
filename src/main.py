from application.services import TaskService
from infrastructure.sqlite.sqlite_database import SQLiteDatabase
from infrastructure.sqlite.sqlite_tasks_repo import SQLiteTaskRepository
from presentation.api.api import API

def main():
    db = SQLiteDatabase()
    repo = SQLiteTaskRepository(db)
    
    service = TaskService(repo)
    
 
    # cli = TaskCLIRich(service)

    # cli.run()
    
    api = API(service)
    api.run()

if __name__ == '__main__':
    main()