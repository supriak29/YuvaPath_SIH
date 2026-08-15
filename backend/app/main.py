from fastapi import FastAPI
from sqlalchemy import text

from app.core.database import engine

app = FastAPI(title="Smart Curriculum API")


@app.get("/")
def root():
    return {"message": "Smart Curriculum API is running"}


@app.get("/health/db")
def database_health():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        return {"database": "connected", "result": result.scalar()}