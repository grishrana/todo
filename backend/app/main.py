from fastapi import FastAPI, HTTPException, Depends
from contextlib import asynccontextmanager
from datetime import datetime, timezone
from typing import Annotated, Any
import random
from dotenv import load_dotenv
from sqlmodel import create_engine, SQLModel, Session
import os
from urllib.parse import quote_plus
from .schema import TaskCreate, TaskUpdate  # pyright: ignore[]
from .models import Task

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASS = quote_plus(str(os.getenv("DB_PASS")))
DB_URL = f"postgresql://{DB_USER}:{DB_PASS}@localhost:5432/smart_todo"


engine = create_engine(DB_URL)


def create_engine_table():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


Session_Dep = Annotated[Session, Depends(get_session)]


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_engine_table()
    yield


data: Any = []

app = FastAPI(root_path="/api/v1", lifespan=lifespan)


@app.get("/")
def hello_world():
    return {"data": DB_USER}


@app.get("/api/v1/show")
async def show_tasks():
    if not data:
        raise HTTPException(status_code=404)
    return {"todo": data}


@app.post("/api/v1/create")
async def create(task: TaskCreate):
    valid_task = task.dict()
    valid_task["id"] = random.randint(1, 1000)
    valid_task["user_id"] = random.randint(1, 1000)
    valid_task["created_at"] = datetime.now(timezone.utc)
    valid_task["completed"] = False
    data.append(valid_task)
    return {"todo": valid_task}


@app.put("/api/v1/update/{id}")
async def update(id: int, task_updated: TaskUpdate):
    updated_fields = task_updated.dict()
    for index, task in enumerate(data):
        if task.get("id") == id:
            for key, value in updated_fields.items():
                task[key] = value

            data[index] = task

            return {"todo": data[index], "updated": True}
    return HTTPException(status_code=404)


@app.delete("/api/v1/delete/{id}", status_code=204)
async def delete(id: int):
    for index, task in enumerate(data):
        if task.get("id") == id:
            data.pop(index)

    else:
        return HTTPException(status_code=404)
