from typing import List
from pydantic import BaseModel

class Challengehistory(BaseModel):
    value: int
    times: int
    parcial_points: int
    isactive: int
    id_user: int
    id_challenge: int