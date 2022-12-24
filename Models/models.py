from pydantic import BaseModel
from typing import Optional, List

class User(BaseModel):
    userID: int
    phoneNumber: str

class APIConfig(BaseModel):
    minSupportedVersion: str

class Place(BaseModel):
    placeID: str
    name: str
    rating: float
    numberOfRatings: int
    address: str
    photoReference: str
    category: str

class Location(BaseModel):
    latitude: float
    longitude: float

class SearchType(BaseModel):
    type: str = ""

class SearchTerm(BaseModel):
    term: str = ""

class PhotoReference(BaseModel):
    reference: str = ""

class NearbyPlacesReturnModel(BaseModel):
    places: List[Place]
    count: int
