from fastapi import FastAPI
from app.database import engine
from app import models
from sqlalchemy import create_engine

app = FastAPI()

# TODO: conditional code that will create_all in dev and use alembic in prod
# Use a synchronous engine to create tables
sync_engine = create_engine("postgresql://postgres:password@db:5432/postgres")
models.Base.metadata.create_all(bind=sync_engine)

@app.get("/")
async def root():
    return {"message": "Hello, World!"}
