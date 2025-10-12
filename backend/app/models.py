from enum import Enum
from sqlmodel import SQLModel, Field
from datetime import datetime, timezone


class PriorityEnum(str, Enum):
    high = "high"
    medium = "medium"
    low = "low"


class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    email: str = Field(unique=True, max_length=255)
    username: str = Field(max_length=255, unique=True)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    pw_hash: str


class Task(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    description: str | None
    user_id: int | None = Field(default=None, foreign_key="user.id")
    priority: PriorityEnum = Field(default=PriorityEnum.medium)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    end_date: datetime
    completed: bool = Field(default=False)
