from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    userID: int
    phoneNumber: str
