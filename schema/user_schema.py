from pydantic import BaseModel
from typing import Optional


class UserSchema(BaseModel):
    id: Optional[int]=None
    name: str
    shortname: str
    user_passw: str