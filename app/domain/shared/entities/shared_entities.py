from dataclasses import dataclass


@dataclass
class Houmer:
    houmerId: int
    firstName: str
    lastName: str
    email: str
    phoneNumber: str

    def __init__(self):
        pass


@dataclass
class Location:
    latitude: float
    longitude: float


@dataclass
class Place:
    placeId: int
    address: str
    location: Location

    def __init__(self):
        pass
