from typing import List
from pydantic import BaseModel

class User(BaseModel):
    id: int | None = None
    email: str
    points: int