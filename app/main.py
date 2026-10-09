from fastapi import FastAPI

from app.api.routes import health

app = FastAPI(
    title="AI Knowledge Assistant",
    version="0.1.0",
    description="Bootstrap API: primer incremento funcional (sin LLM).",
)

app.include_router(health.router)
from fastapi import FastAPI

from app.api.routes import chat, health

app = FastAPI(
    title="AI Knowledge Assistant",
    version="0.1.0",
    description="Bootstrap API: primer incremento funcional (sin LLM).",
)

app.include_router(health.router)
app.include_router(chat.router, prefix="/api/v1")
