from typing import List
from pydantic import BaseModel

class Redeemhistory(BaseModel):
    value: int
    times: int
    id_user: int
    id_product: int