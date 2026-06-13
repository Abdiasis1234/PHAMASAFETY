"""Shared Gemini model factory — API key OR Vertex ADC."""
from __future__ import annotations

import os
from contextlib import contextmanager

from langchain_google_genai import ChatGoogleGenerativeAI


@contextmanager
def _without_env_keys(*keys: str):
    """Temporarily remove env vars that confuse the Google Gen AI SDK.

    Vertex express keys (AQ.*) must not share the environment with
    GOOGLE_CLOUD_LOCATION / GOOGLE_CLOUD_PROJECT — the SDK treats that as
    ADC mode and silently drops the API key.
    """
    saved = {k: os.environ.pop(k) for k in keys if k in os.environ}
    try:
        yield
    finally:
        os.environ.update(saved)


def build_gemini_model() -> ChatGoogleGenerativeAI:
    """Build ChatGoogleGenerativeAI using an express API key or Vertex ADC."""
    model = os.getenv("MODEL", "gemini-3.5-flash")
    api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
    use_vertex = os.getenv("GOOGLE_GENAI_USE_VERTEXAI", "").lower() in (
        "1",
        "true",
    )

    if api_key and use_vertex:
        # Vertex express mode — API key only. Do NOT pass project/location.
        with _without_env_keys(
            "GOOGLE_API_KEY",
            "GEMINI_API_KEY",
            "GOOGLE_CLOUD_PROJECT",
            "GOOGLE_CLOUD_LOCATION",
        ):
            return ChatGoogleGenerativeAI(
                model=model,
                google_api_key=api_key,
                vertexai=True,
            )

    if api_key:
        return ChatGoogleGenerativeAI(model=model, google_api_key=api_key)

    project = os.getenv("GOOGLE_CLOUD_PROJECT")
    if not project:
        raise ValueError(
            "No GEMINI_API_KEY / GOOGLE_API_KEY and no GOOGLE_CLOUD_PROJECT. "
            "Either set a Vertex express API key (leave GOOGLE_CLOUD_LOCATION "
            "unset) or configure ADC (scripts/setup-adc.ps1)."
        )

    return ChatGoogleGenerativeAI(
        model=model,
        vertexai=True,
        project=project,
        location=os.getenv("GOOGLE_CLOUD_LOCATION", "us-central1"),
    )
