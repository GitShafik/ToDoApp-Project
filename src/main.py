from application.service import TaskService
from infrastructure.inmemory.inmemory import InMemoryTaskDB
from interface.cli_rich.cli_rich import TaskCLIRich

def main():
    print("startar i main")
    db = InMemoryTaskDB()
    service = TaskService(db)
    #cli = TaskCLI(service)
    cli = TaskCLIRich(service)

    cli.run()

if __name__ == '__main__':
    main()