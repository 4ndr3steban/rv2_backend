from typing import List
from pydantic import BaseModel

class Impact(BaseModel):
    id: int
    title: str
    number: str
    units: str
    description: str
    image: str