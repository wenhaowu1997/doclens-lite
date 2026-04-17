"""
Document-related API routes for DocLens Lite.

This module defines endpoints related to document and text processing,
including text summarization.
"""

from fastapi import APIRouter
from app.models.schemas import SummarizeRequest, SummarizeResponse
from app.services.summarizer import summarize_text

router = APIRouter(tags=["document"])


@router.post("/summarize", response_model=SummarizeResponse)
def summarize(request: SummarizeRequest) -> SummarizeResponse:
    """
    Summarize the input text.

    This endpoint receives text input, generates a simple baseline summary,
    and returns the summary along with basic length information.

    Args:
        request (SummarizeRequest): The input payload containing text.

    Returns:
        SummarizeResponse: The generated summary and metadata.
    """
    summary = summarize_text(request.text)

    return SummarizeResponse(
        summary=summary,
        original_length=len(request.text),
        summary_length=len(summary),
    )