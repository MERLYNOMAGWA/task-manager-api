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
