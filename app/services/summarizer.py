"""
Summarization service for DocLens Lite.

This module contains the core text summarization logic used by the API.
The current implementation is a simple baseline summarizer that returns
the first few sentences of the input text.
"""


def summarize_text(text: str, max_sentences: int = 3) -> str:
    """
    Generate a simple baseline summary from input text.

    The current implementation splits the input text into sentence-like
    chunks and returns the first few non-empty sentences.

    Args:
        text (str): The input text to summarize.
        max_sentences (int): Maximum number of sentences to include
            in the summary.

    Returns:
        str: A simple summary string.
    """
    text = text.strip()
    if not text:
        return ""

    separators = [".", "!", "?", "。", "！", "？", "\n"]
    sentences = [text]

    for sep in separators:
        temp = []
        for chunk in sentences:
            temp.extend(chunk.split(sep))
        sentences = temp

    sentences = [s.strip() for s in sentences if s.strip()]
    summary_sentences = sentences[:max_sentences]

    if not summary_sentences:
        return text[:300]

    return " ".join(summary_sentences)