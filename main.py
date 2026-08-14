from fastapi import FastAPI
from utils.db import Base, engine
from models.task import Task
from routes.task_router import task_router

app = FastAPI(title="Task Management API", description="API for managing tasks")

Base.metadata.create_all(bind=engine)

# Include the task router
app.include_router(task_router)

@app.get("/")
def read_root():
    return {"message": "Hello World"}