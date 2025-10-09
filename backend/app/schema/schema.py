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


# Schema for JWT
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


# schema for user
class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None


class UserInDB(User):
    hashed_password: str
