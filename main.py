from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from enum import Enum
from typing import Optional, List

app = FastAPI()

class StatusEnum(str, Enum):
   pending = "pending"
   in_progress = "in_progress"
   completed = "completed"

class PriorityEnum(str, Enum):
   low = "low"
   medium = "medium"
   high = "high"

class TaskCreate(BaseModel):
   title: str
   description: Optional[str] = None
   status: StatusEnum
   priority: PriorityEnum

class TaskUpdate(BaseModel):
   title: Optional[str] = None
   description: Optional[str] = None
   status: Optional[StatusEnum] = None
   priority: Optional[PriorityEnum] = None

class Task(TaskCreate):
   id: int


tasks = []
task_id_counter = 1

@app.get("/tasks", response_model=List[Task])
def get_tasks():
   return tasks

@app.post("/tasks", response_model=Task, status_code=201)
def create_task(task: TaskCreate):
   global task_id_counter
   new_task = Task(id=task_id_counter, **task.dict())
   tasks.append(new_task)
   task_id_counter += 1
   return new_task

@app.put("/tasks/{id}", response_model=Task)
def update_task(id: int, updated_task: TaskUpdate):
   for task in tasks:
      if task.id == id:
         if updated_task.title is not None:
            task.title = updated_task.title
         if updated_task.description is not None:
            task.description = updated_task.description
         if updated_task.status is not None:
            task.status = updated_task.status
         if updated_task.priority is not None:
            task.priority = updated_task.priority
         return task
   raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{id}", status_code=204)
def delete_task(id: int):
   for task in tasks:
      if task.id == id:
         tasks.remove(task)
         return
   raise HTTPException(status_code=404, detail="Task not found")
