"""
Schemas for the DocLens Lite API.

This module defines the request and response data models used by the API.
All schemas are implemented using Pydantic for data validation and
automatic documentation generation in FastAPI.
"""
from pydantic import BaseModel, Field


class SummarizeRequest(BaseModel):
    """
    Request schema for the summarize API.

    This model defines the expected input payload when calling the
    /api/summarize endpoint.

    Attributes:
        text (str): The text to be summarized. Must be a non-empty string.
    """
    text: str = Field(..., min_length=1, description="Text to summarize")
    # pydantic 格式定義輸入資料模型，繼承自 BaseModel
    # 定義 API 輸入欄位：
    # - 型別：str（字串）
    # - ...：代表必填欄位（required）
    # - min_length=1：字串至少要有 1 個字元（避免空字串）
    # - description：顯示在 Swagger (/docs) 中的欄位說明


class SummarizeResponse(BaseModel):
    """
    Response schema for the summarize API.

    This model defines the structure of the response returned by the
    /api/summarize endpoint.

    Attributes:
        summary (str): The generated summary of the input text.
        original_length (int): The length of the original input text.
        summary_length (int): The length of the generated summary.
    """
    summary: str
    original_length: int
    summary_length: int