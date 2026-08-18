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

