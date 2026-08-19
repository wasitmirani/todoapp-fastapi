from dtos.task_dtos import TaskCreateDto
from sqlalchemy.orm import Session
from models.task import Task
from datetime import datetime
from fastapi import HTTPException

def create_task(task: TaskCreateDto,db: Session | None = None) -> TaskCreateDto:
    data = task.model_dump()
    new_task = Task(title=data['title'], 
    description=data['description'], 
    completed=data['completed'],
    created_at=datetime.now(),
    updated_at=datetime.now()
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task



def get_tasks(db:Session | None = None):
    if db is None:
        raise HTTPException(status_code=400, detail="Database session not found")
    tasks= db.query(Task).order_by(Task.created_at.desc()).all()
    return {"tasks": tasks,"message": "Tasks fetched successfully","status": "success"}


def get_task(id:int, db:Session | None = None):
    if db is None:
        raise HTTPException(status_code=400, detail="Database session not found")
    task  =db.query(Task).where(Task.id == id).first()
    if task is None:
         raise HTTPException(status_code=404, detail="Task not found")
    return {"task": task,"message": "Task fetched successfully","status": "success"}

def update_task(id:int,task: TaskCreateDto, db:Session | None = None):
    if db is None:
        raise HTTPException(status_code=400, detail="Database session not found")
    task_data = db.query(Task).where(Task.id == id).first()
    if task_data is None:
        raise HTTPException(status_code=404, detail="Task not found")
    task_data.title = task.title
    task_data.description = task.description
    task_data.completed = task.completed
    task_data.updated_at = datetime.now()
    db.commit()
    db.refresh(task_data)
    return {"task": task_data,"message": "Task updated successfully","status": "success"}