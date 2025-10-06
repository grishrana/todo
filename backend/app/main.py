from fastapi import FastAPI, HTTPException, HTMLResponse
from pathlib import Path
from contextlib import asynccontextmanager
from datetime import datetime, timezone
from sqlmodel import Session, select
from .schema import TaskCreate, TaskUpdate, Response  # pyright: ignore[]
from .core import Session_Dep, engine, create_engine_table
from .models import Task
from fastapi.middleware.cors import CORSMiddleware


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


origins = [
    "http://localhost:8080",
    "http://localhost:5173",  # vite, svelte
    "http://localhost:3000",  # react, next
]

app = FastAPI(root_path="/api/v1", lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_headers=["*"],
    allow_methods=["*"],
)

@app.get("/", response_class=HTMLResponse)
def read_index():
    html_path = Path(__file__).parent / "wip" / "index.html"
    return html_path.read_text()


@app.get("/api/v1/show", response_model=Response[list[Task]])
async def show_tasks(session: Session_Dep):
    data = session.exec(select(Task)).all()
    return {"data": data}


@app.get("/api/v1/{id}", response_model=Response[Task])
async def show_task(id: int, session: Session_Dep):
    data = session.get(Task, id)
    if not data:
        raise HTTPException(status_code=404)
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
        raise HTTPException(status_code=404)
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
        raise HTTPException(status_code=404)
    else:
        session.delete(task)
        session.commit()
