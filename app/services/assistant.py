"""Servicio del asistente (implementación local de bootstrap, sin LLM)."""

import asyncio

PROVIDER_NAME = "bootstrap-local"

_KNOWN_ANSWERS: dict[str, str] = {
    "fastapi": (
        "FastAPI es un framework web moderno de Python para construir APIs "
        "con tipado, validación automática y documentación OpenAPI."
    ),
    "pydantic": (
        "Pydantic es una librería de Python para validar y serializar datos "
        "usando anotaciones de tipo."
    ),
    "asyncio": (
        "AsyncIO es la librería estándar de Python para programación "
        "concurrente con async/await."
    ),
}


class AssistantService:
    """Genera respuestas locales y deterministas.

    En módulos posteriores esta clase se reemplazará por una que llame a un LLM,
    manteniendo el mismo contrato (`answer` + `provider`).
    """

    provider = PROVIDER_NAME

    async def answer(self, question: str) -> str:
        # Simula una operación de I/O (en el futuro: llamada a un LLM).
        await asyncio.sleep(0)
        normalized = question.lower()
        for keyword, text in _KNOWN_ANSWERS.items():
            if keyword in normalized:
                return text
        return (
            "Respuesta de bootstrap: aún no hay un modelo de lenguaje conectado. "
            f"Recibí tu pregunta: {question.strip()}"
        )


def get_assistant_service() -> AssistantService:
    """Dependencia de FastAPI: permite inyectar/reemplazar el servicio en tests."""
    return AssistantService()
