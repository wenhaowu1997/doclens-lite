from fastapi import FastAPI
from app.routes.health import router as health_router

app = FastAPI(
    title="DocLens Lite",
    version="0.1.0",
    description="A minimal document summarization API built with FastAPI."
)

app.include_router(health_router, prefix="/api")