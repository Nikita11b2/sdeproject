from fastapi import FastAPI
from .routers import configurations
from .database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(configurations.router)
