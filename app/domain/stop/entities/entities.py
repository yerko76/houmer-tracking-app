from datetime import datetime
from enum import Enum
from dataclasses import dataclass
from app.domain.shared.entities.shared_entities import Place


class StopEnum(str, Enum):
    COMPLETED = "COMPLETED"
    ARRIVED_TO_LOCATION = "ARRIVED_TO_LOCATION"
    IN_PROGRESS = "IN_PROGRESS"
    NOT_STARTED = "NOT_STARTED"
    VISITING = "VISITING"


@dataclass
class Stop:
    stopId: str
    place: Place
    status: StopEnum
    start: datetime
    end: datetime
    visitingStart: datetime
    visitingEnd: datetime

    def __init__(self):
        pass
