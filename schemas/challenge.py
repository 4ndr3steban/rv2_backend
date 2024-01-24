from typing import List
from pydantic import BaseModel

class Challenge(BaseModel):
    id: int
    category: str
    points: int
    completed: int
    name: str
    description: str
    icon: str
    image: str
    bg_color: str
    limit_of_completion: int
    form: str
    challenge_type: str