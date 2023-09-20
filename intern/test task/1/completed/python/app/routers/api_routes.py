from fastapi import APIRouter

from routers.routes import ping, shutdown, validate_phone_number


def create_api_router() -> APIRouter:
    api_router = APIRouter()
    api_router.include_router(ping.router)
    api_router.include_router(shutdown.router)
    api_router.include_router(validate_phone_number.router, tags=["validator"])
    return api_router


router = create_api_router()
