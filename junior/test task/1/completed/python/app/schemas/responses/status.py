from pydantic import BaseModel


class WorkStatus(BaseModel):
    is_started: bool
