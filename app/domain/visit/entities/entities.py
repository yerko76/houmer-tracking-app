from typing import List
from datetime import date, datetime
from dataclasses import dataclass
from app.domain.shared.entities.shared_entities import Houmer, Location
from app.domain.stop.entities.entities import Stop


@dataclass
class Visit:
    visitId: str
    stops: List[Stop]
    houmer: Houmer
    scheduledAt: date
    cretedAt: datetime
    currentLocation: Location

    def __init__(self):
        pass
