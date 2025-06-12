from fastapi import FastAPI

from application.services import TaskService
from presentation.api.routes import root_router, task_query_router
from presentation.api.service_manager import ServiceManager

class API:
    def __init__(self, service: TaskService):
        ServiceManager.set_service(service)
        self.app = FastAPI()
        
        self.app.include_router(root_router)
        self.app.include_router(task_query_router)
        
        
    def run(self):
        import uvicorn
        uvicorn.run(self.app, host="0.0.0.0", port=8100)