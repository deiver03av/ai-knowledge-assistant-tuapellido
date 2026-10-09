from fastapi import APIRouter

from app.schemas.info import InfoResponse

router = APIRouter(tags=["info"])


@router.get("/info", response_model=InfoResponse)
async def info() -> InfoResponse:
    """Información básica del proyecto."""
    return InfoResponse(
        name="AI Knowledge Assistant",
        version="0.1.0",
        environment="development",
        llm_enabled=False,
    )
