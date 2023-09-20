from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from routers.api_routes import router
from utils.logger import log


def create_application() -> FastAPI:
    application = FastAPI(
        docs_url="/docs",
        redoc_url=None,
    )
    application.include_router(router=router)

    def custom_openapi():
        if application.openapi_schema:
            return app.openapi_schema
        openapi_schema = get_openapi(
            title="Phone Validator",
            version="1.0.prod",
            openapi_version = "3.0.0",
            description="API for validating phone numbers",
            routes=application.routes,
        )
        openapi_schema["components"]["schemas"] = {
            "Success": {
                "title": "Success",
                "description": "This response is returned if a valid phone number is transmitted",
                "type": "object",
                "properties": {
                    "status": {
                        "title": "status",
                        "description": "Validation result",
                        "type": "boolean",
                    },
                    "normalized": {
                        "title": "normalized",
                        "description": "Normalized value of the form +7-###-###-####, where # is a digit",
                        "type": "string",
                        "example": "+7-912-123-4567",
                    }
                },
            },
            "Error": {
                "title": "Error",
                "description": "This response is returned if an invalid phone number is transmitted",
                "type": "object",
                "properties": {
                    "status": {
                        "title": "status",
                        "description": "\"Validation result\" A case-sensitive path is specified in the specification. The service must process the query parameters that are declared in the specification, the other parameters must be ignored.",
                        "type": "boolean",
                    },
                },
            },
        }
        application.openapi_schema = openapi_schema
        return application.openapi_schema

    application.openapi = custom_openapi

    @application.on_event("startup")
    async def startup() -> None:
        return log.info("Application startup")

    @application.on_event("shutdown")
    async def shutdown() -> None:
        return log.warning("Application shutdown")

    return application


app = create_application()
