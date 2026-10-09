from fastapi import APIRouter, Depends

from app.schemas.chat import ChatRequest, ChatResponse
from app.services.assistant import AssistantService, get_assistant_service

router = APIRouter(tags=["chat"])


@router.post("/chat", response_model=ChatResponse)
async def chat(
    payload: ChatRequest,
    service: AssistantService = Depends(get_assistant_service),
) -> ChatResponse:
    """Recibe una pregunta (ya validada por Pydantic) y delega al servicio."""
    answer = await service.answer(payload.question)
    return ChatResponse(answer=answer, provider=service.provider)