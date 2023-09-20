from pydantic import BaseModel


class ValidatedPhoneNumber(BaseModel):
    status: bool = True
    normalized: str | None = "+7-982-123-4567"
