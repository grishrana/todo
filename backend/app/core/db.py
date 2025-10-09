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


fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "$argon2id$v=19$m=65536,t=3,p=4$wagCPXjifgvUFBzq4hqe3w$CYaIb8sB+wtD+Vu/P4uod1+Qof8h+1g7bbDlBID48Rc",
        "disabled": False,
    }
}


engine = create_engine(DB_URL)


def create_engine_table():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


Session_Dep = Annotated[Session, Depends(get_session)]
