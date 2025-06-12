from application.services import TaskService

class ServiceManager:
    _instance = None
    
    @classmethod
    def set_service(cls, service: TaskService) -> None:
        cls._instance = service
    
    @classmethod
    def get_service(cls) -> TaskService:
        return cls._instance
    
    @classmethod
    def create_task(cls) -> TaskService:
        return cls._instance