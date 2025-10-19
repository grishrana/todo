from sqlmodel import create_engine, Session, SQLModel
from fastapi import Depends
from .config import settings
from typing import Annotated


engine = create_engine(settings.db_url)


def create_engine_table():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


Session_Dep = Annotated[Session, Depends(get_session)]
