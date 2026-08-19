from fastapi import APIRouter,Depends
from controllers.task_controller import create_task,get_tasks,get_task,update_task
from dtos.task_dtos import TaskCreateDto
from utils.db import get_db
from sqlalchemy.orm import Session

task_router = APIRouter(prefix="/tasks", tags=["tasks"])


@task_router.post('/store')
def store_task(task: TaskCreateDto, db: Session = Depends(get_db)):
    return {"message": "Task created successfully", "task": create_task(task, db)}

@task_router.get('/items')
def get_list(db: Session = Depends(get_db)):
    return get_tasks(db)

@task_router.get('/{id}')
def show_task(id:int, db: Session = Depends(get_db)):
    return get_task(id, db)


@task_router.put('/{id}')
def update(id:int ,task: TaskCreateDto, db: Session = Depends(get_db)):
    return update_task(id, task, db)