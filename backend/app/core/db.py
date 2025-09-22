import os
from urllib.parse import quote_plus
from dotenv import load_dotenv
from sqlmodel import create_engine, Session, SQLModel
from fastapi import Depends
from typing import Annotated


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
