from fastapi import APIRouter
from controllers.task_controller import create_task
from dtos.task_dtos import TaskCreateDto

task_router = APIRouter(prefix="/tasks", tags=["tasks"])


@task_router.post('/store')
def store_task(task: TaskCreateDto):
    return create_task(task)