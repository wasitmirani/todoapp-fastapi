from pydantic import BaseModel


class TaskCreateDto(BaseModel):
    title: str
    description: str
    completed: bool

class TaskUpdateDto(BaseModel):
    title: str
    description: str
    completed: bool

class TaskResponseDto(BaseModel):
    id: int
    title: str
    description: str