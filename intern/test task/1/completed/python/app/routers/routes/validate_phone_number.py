from fastapi import APIRouter
from fastapi.responses import JSONResponse

from core.parser import PhoneParser
from schemas.validate import ValidatedPhoneNumber
from utils.logger import log

router = APIRouter()


@router.get(
    path="/validatePhoneNumber",
    description="API for validating phone numbers",
    response_model=ValidatedPhoneNumber,
    responses={
        200: {
            "description": "Successful operation",
            "content": {
                "application/json": {
                    "schema": {
                        "allOf":{
                        "$ref": "/openapi.json#/components/schemas/Success",
                        "$ref": "/openapi.json#/components/schemas/Error",
                    },}
                },
            },
        },
        400: {
            "description": "Invalid request",
        },
        404: {
            "description": "Not found",
        },
    },
)
async def validate_phone_number(phone_number: str) -> JSONResponse:
    if phone_number is None or len(phone_number) != 11:
        response = ValidatedPhoneNumber(status=False, normalized=None)
        return JSONResponse(content=response.dict(),
                            status_code=400, headers=None)

    log.info(f"phone_number: {phone_number}")
    headers = {'Content-Type': 'application/json'}
    normalized = PhoneParser(raw=phone_number).parse()
    response = ValidatedPhoneNumber(
        status=True if normalized is not None else False,
        normalized=normalized,
    )

    return JSONResponse(
        content=response.dict(),
        status_code=200,
        headers=headers,
    )
