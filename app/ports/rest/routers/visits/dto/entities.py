from typing import List
from pydantic import BaseModel


class Place(BaseModel):
    placeId: int


class Location(BaseModel):
    longitude: float
    latitude: float


class VisitRequest(BaseModel):
    currentLocation: Location
    places: List[Place]
    date: str


class Stop(BaseModel):
    stopId: str
    description: str
    placeId: int
    location: Location


class StopResponse(BaseModel):
    stopId: str
    description: str
    location: Location
    timeInLocation: str


class VisitResponse(BaseModel):
    visitId: str
    stops: List[Stop]


class UpdateLocation(BaseModel):
    currentLocation: Location
