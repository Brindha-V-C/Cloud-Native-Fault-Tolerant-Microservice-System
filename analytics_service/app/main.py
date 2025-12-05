from fastapi import FastAPI
from .routes import router

app = FastAPI(
    title="Analytics Service",
    description="Tracks user events and provides metrics",
    version="1.0.0"
)

app.include_router(router)
