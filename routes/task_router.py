from fastapi import APIRouter,Depends
from controllers.task_controller import create_task
from dtos.task_dtos import TaskCreateDto
from utils.db import get_db
from sqlalchemy.orm import Session

task_router = APIRouter(prefix="/tasks", tags=["tasks"])


@task_router.post('/store')
def store_task(task: TaskCreateDto, db: Session = Depends(get_db)):
    return {"message": "Task created successfully", "task": create_task(task, db)}