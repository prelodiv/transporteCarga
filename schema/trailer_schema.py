from pydantic import BaseModel
from typing import Optional


class TrailerSchema(BaseModel):
    id: Optional[int]=None
    trailer_type: str
    number_plate: str
    capacity: str
    status: str
    cargo_type: str