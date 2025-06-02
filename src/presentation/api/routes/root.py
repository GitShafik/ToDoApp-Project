import time
import datetime

from fastapi import APIRouter

router = APIRouter()
start_time = time.time()

@router.get("/")
def root():
    uptime = time.time() - start_time
    uptime = datetime.timedelta(seconds=uptime)
    return {
        "status": f"App is running... {uptime}",
        "message": "Welcome! This is the backend API for the ToDo app."
    }
