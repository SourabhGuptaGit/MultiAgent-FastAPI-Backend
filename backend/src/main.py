import os
from contextlib import asynccontextmanager
from fastapi import FastAPI

from api.chat.routing import router as chat_router
from api.db import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    # before app startup
    init_db()
    yield
    # After app startup

app = FastAPI(lifespan=lifespan)
app.include_router(chat_router, prefix="/api/chats")

env_variables = ["PORT","PORT","NOTE", "POSTGRES_USER","POSTGRES_PASS","POSTGRES_DB"]

@app.get("/")
def home():
    return {
        "message": "Welcome to your first FastAPI.",
        # "environment": {key: os.getenv(key) for key in env_variables}
    }


