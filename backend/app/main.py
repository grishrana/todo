from fastapi import FastAPI, HTTPException, Depends
from contextlib import asynccontextmanager
from datetime import datetime, timezone
from typing import Annotated, Any
from dotenv import load_dotenv
from sqlmodel import create_engine, SQLModel, Session, select
import os
from urllib.parse import quote_plus
from .schema import TaskCreate, TaskUpdate, Response  # pyright: ignore[]
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
    with Session(engine) as session:
        if not session.exec(select(Task)).first():
            session.add(
                Task(
                    title="Develop Smart Todo",
                    description="Complete Backeend with PSG, FASTApi and sqlmodel endpoints",
                    end_date=datetime(2025, 10, 25, 0, 0, tzinfo=timezone.utc),
                )
            )

            session.commit()
    yield


data: Any = []

app = FastAPI(root_path="/api/v1", lifespan=lifespan)


@app.get("/", response_model=Response[str])
def hello_world():
    return {"data": "Hello World"}


@app.get("/api/v1/show", response_model=Response[list[Task]])
async def show_tasks(session: Session_Dep):
    data = session.exec(select(Task)).all()
    return {"data": data}


@app.get("/api/v1/{id}", response_model=Response[Task])
async def show_task(id: int, session: Session_Dep):
    data = session.get(Task, id)
    if not data:
        return HTTPException(404)
    else:
        return {"data": data}


@app.post("/api/v1/create", status_code=201, response_model=Response[Task])
async def create(task: TaskCreate, session: Session_Dep):
    db_task = Task.model_validate(task)
    session.add(db_task)
    session.commit()
    session.refresh(db_task)
    return {"data": db_task}


@app.put("/api/v1/update/{id}", response_model=Response[Task])
async def update(id: int, task_updated: TaskUpdate, session: Session_Dep):
    task = session.get(Task, id)
    if not task:
        return HTTPException(status_code=404)
    else:
        task.title = task_updated.title
        task.description = task_updated.description
        task.priority = task_updated.priority
        task.end_date = task_updated.end_date
        task.completed = task_updated.completed
        session.add(task)
        session.commit()
        session.refresh(task)
        return {"data": task}


@app.delete("/api/v1/delete/{id}", status_code=204)
async def delete(id: int, session: Session_Dep):
    task = session.get(Task, id)
    if not task:
        return HTTPException(status_code=404)
    else:
        session.delete(task)
        session.commit()
