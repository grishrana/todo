from typing import Annotated
from fastapi import FastAPI, HTTPException, Depends, status
from contextlib import asynccontextmanager
from datetime import datetime, timezone, timedelta
from sqlmodel import Session, select
from .schema import (
    TaskCreate,
    TaskUpdate,
    Response,
    Token,
    User,
)  # pyright: ignore[]
from .core.db import (
    Session_Dep,
    engine,
    create_engine_table,
)
from .core.security import (
    ACCESS_TOKEN_EXPIRE_MINUTES,
    get_current_user,
    auth_depend,
    create_access_token,
    authenticate_user,
)
from .models import Task
from .core.db import fake_users_db
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm


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


async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)],
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive User")
    return current_user


@app.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]) -> Token:
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")


@app.get("/users/me")
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_active_user)],
):
    return current_user


@app.get("/", response_model=Response[str])
def hello_world():
    return {"data": "Hello World"}


@app.get("/show", response_model=Response[list[Task]])
async def show_tasks(session: Session_Dep, token: auth_depend):
    data = session.exec(select(Task)).all()
    return {"data": data}


@app.get("/show/{id}", response_model=Response[Task])
async def show_task(id: int, session: Session_Dep):
    data = session.get(Task, id)
    if not data:
        raise HTTPException(status_code=404)
    return {"data": data}


@app.post("/create", status_code=201, response_model=Response[Task])
async def create(task: TaskCreate, session: Session_Dep):
    db_task = Task.model_validate(task)
    session.add(db_task)
    session.commit()
    session.refresh(db_task)
    return {"data": db_task}


@app.put("/update/{id}", response_model=Response[Task])
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


@app.delete("/delete/{id}", status_code=204)
async def delete(id: int, session: Session_Dep):
    task = session.get(Task, id)
    if not task:
        raise HTTPException(status_code=404)
    else:
        session.delete(task)
        session.commit()
