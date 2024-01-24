from typing import List
from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    cost: int
    category: str
    image: str