from core.database import Base, engine
from core.middleware.cors import setup_cors_middleware
from fastapi import FastAPI, Response
from loguru import logger
from routers.api_routes import router
from starlette import status


def create_application() -> FastAPI:

    application = FastAPI(
        title="Pets",
        version="0.1",
        docs_url="/docs",
        redoc_url=None,
    )
    setup_cors_middleware(app=application)
    application.include_router(router=router)

    @application.on_event("startup")
    async def startup() -> None:
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        return logger.info("Application startup")

    @application.on_event("shutdown")
    async def shutdown() -> None:
        return logger.warning("Application shutdown")

    @application.get(
        path="/",
        status_code=status.HTTP_200_OK,
        summary="Check health status",
        description="Check health status (´♡‿♡`)",
    )
    async def healthcheck() -> Response:
        return {"ok": True}

    return application


app = create_application()
