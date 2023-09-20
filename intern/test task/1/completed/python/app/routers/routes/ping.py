from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()


@router.get(
    path="/ping",
)
async def ping() -> JSONResponse:
    return JSONResponse(content="", status_code=200, headers=None)
