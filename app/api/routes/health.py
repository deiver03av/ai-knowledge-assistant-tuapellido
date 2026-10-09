from fastapi import APIRouter

router = APIRouter(tags=["health"])


@router.get("/health")
async def health() -> dict[str, str]:
    """Indica que la aplicación está viva."""
    return {"status": "ok"}
