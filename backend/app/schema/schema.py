from enum import Enum
from sqlmodel import SQLModel, Field
from datetime import datetime
from pydantic import BaseModel
from typing import TypeVar, Generic

T = TypeVar("T")


class Response(BaseModel, Generic[T]):
    data: T


# schema for request and response
class PriorityEnum(str, Enum):
    high = "high"
    medium = "medium"
    low = "low"


class TaskCreate(SQLModel):
    title: str
    description: str | None
    priority: PriorityEnum = Field(default=PriorityEnum.medium)
    end_date: datetime


class TaskUpdate(SQLModel):
    title: str
    description: str | None
    priority: PriorityEnum = Field(default=PriorityEnum.medium)
    end_date: datetime
    completed: bool = Field(default=False)
