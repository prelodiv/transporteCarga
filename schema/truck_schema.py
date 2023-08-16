from pydantic import BaseModel
from typing import Optional


class TruckSchema(BaseModel):
    id: Optional[int]=None
    model: str
    number_plate: str
    capacity: str
    status: str