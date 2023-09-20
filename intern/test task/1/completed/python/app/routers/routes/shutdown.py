import sys

from fastapi import APIRouter

router = APIRouter()


@router.get(path="/shutdown")
async def shutdown() -> None:
    return sys.exit()
