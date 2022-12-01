from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    userID: int
    phoneNumber: str

class APIConfig(BaseModel):
    minSupportedVersion: str

class Coordinates(BaseModel):
    latitude: int
    longtitude: int