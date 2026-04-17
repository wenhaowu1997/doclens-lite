"""
Main application entry point for DocLens Lite.

This module creates the FastAPI app instance and registers all API routes.
"""

from fastapi import FastAPI
from app.routes.health import router as health_router
from app.routes.document import router as document_router

app = FastAPI(
    title="DocLens Lite",
    version="0.1.0",
    description="A minimal document summarization API built with FastAPI."
)

app.include_router(health_router, prefix="/api")
app.include_router(document_router, prefix="/api")