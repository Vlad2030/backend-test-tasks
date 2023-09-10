import typing

from models.pets import PetsDatabase
from schemas.pets import PetsSchema, DeletePets
from sqlalchemy import delete, select, insert
from sqlalchemy.ext.asyncio import AsyncSession


class Pets:
    def __init__(self, session) -> None:
        self.session: AsyncSession = session

    async def create(self, pet: PetsSchema) -> None:
        query = insert(PetsDatabase).values(**pet)
        result = await self.session.execute(query)
        await self.session.commit()
        return result.scalars().first()

    async def get_all(self, items: int) -> typing.List[PetsSchema]:
        query = select(PetsDatabase).limit(items)
        result = await self.session.execute(query)
        return result.scalars().all()

    async def get_one_by_id(
            self,
            id: int,
    ) -> typing.Union[PetsSchema, None]:
        query = select(PetsDatabase).where(PetsDatabase.id==id)
        result = await self.session.execute(query)
        return result.scalars().first()

    async def delete_by_id(
            self,
            id: int,
    ) -> typing.Union[PetsSchema, None]:
        query = delete(PetsDatabase).where(PetsDatabase.id==id)
        result = await self.session.execute(query)
        if result is None:
            return result
        await self.session.flush()
        await self.session.commit()
        return result

    async def delete_by_ids(
            self,
            ids: list[int],
    ) -> DeletePets:
        deleted = int()
        errors = list()
        for id in ids:
            query = delete(PetsDatabase).where(PetsDatabase.id==id)
            result = await self.session.execute(query)
            if result is None:
                errors.append({
                    "id": id,
                    "error": "Pet with the matching ID was not found.",
                })
            deleted += 1
        await self.session.flush()
        await self.session.commit()
        return DeletePets(deleted, errors)
