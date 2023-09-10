from core.crud.pets import Pets
from core.database import AsyncSession, get_async_session
from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse
from schemas.pets import PetsSchema


router = APIRouter(prefix="/pets")


@router.get(path="/pets/")
async def get_pets(
        limit: int = 20,
        session: AsyncSession = Depends(get_async_session),
) -> JSONResponse:
    pets = Pets(session)
    pets_list = await pets.get_all(items=limit)
    return {
        "count": len(pets_list),
        "items": pets_list,
    }


@router.post(path="/pets/")
async def add_pet(
        pet: PetsSchema,
        session: AsyncSession = Depends(get_async_session),
) -> JSONResponse:
    pets = Pets(session)
    created_pet = await pets.create(pet)
    return created_pet


@router.delete(path="/pets/")
async def delete_pets(
        ids: list[int],
        session: AsyncSession = Depends(get_async_session),
) -> JSONResponse:
    pets = Pets(session)
    deleted_pets = await pets.delete_by_ids(ids)
    return deleted_pets
