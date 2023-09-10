from fastapi import APIRouter
from routers.routes import mexc, telegram


def create_api_router() -> APIRouter:
    api_router = APIRouter()
    api_router.include_router(mexc.router, tags=["mexc"])
    api_router.include_router(telegram.router, tags=["telegram"])
    return api_router


router = create_api_router()
