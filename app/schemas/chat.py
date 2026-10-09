from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    """Entrada del endpoint de chat."""

    question: str = Field(
        ...,
        min_length=3,
        max_length=2000,
        description="Pregunta del usuario (3 a 2000 caracteres).",
        examples=["¿Qué es FastAPI?"],
    )


class ChatResponse(BaseModel):
    """Salida del endpoint de chat."""

    answer: str
    provider: str
    