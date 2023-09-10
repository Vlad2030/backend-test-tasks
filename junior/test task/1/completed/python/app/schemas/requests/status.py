from pydantic import BaseModel


class WorkStatusRequest(BaseModel):
    action: str
