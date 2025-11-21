import os
from fastapi import FastAPI


app = FastAPI()
APP_PORT = int(os.getenv("FASTPORT")) if os.getenv("FASTPORT", "").isdigit() else "Not Known"

@app.get("/")
def home():
    return {"message": "Welcome to your first FastAPI.", "Port": APP_PORT}

