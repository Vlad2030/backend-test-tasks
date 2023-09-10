from pydantic import BaseModel


class PetsSchema(BaseModel):
    name: str
    age: int
    type: str


class PetsList(BaseModel):
    count: int
    items: list[PetsSchema]


class DeletePets(BaseModel):
    deleted: int
    errors: list[dict]
