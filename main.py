from fastapi import FastAPI
from utils.db import Base, engine
from models.task import Task

app = FastAPI(title="Task Management API", description="API for managing tasks")

Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "Hello World"}