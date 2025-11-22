import os
from sqlmodel import create_engine, Session, SQLModel


DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise NotImplementedError("`DATABASE_URL` needs to be defined.")

DATABASE_URL.replace("postgresql://", "postgresql+psycopg://")

engine = create_engine(DATABASE_URL, connect_args={"connect_timeout": 5})

def init_db():
    print(f"Creating database tables ...")
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session