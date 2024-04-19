from pydantic import BaseModel
from typing import Optional

class AccountModel(BaseModel):
    number: str
    balance: float = 0.0
    type: str
    owner: Optional[str] = None
    

class PersonModel(BaseModel):
    name: str
    age: int
    country: str
    identity: str
    