from typing import Protocol, List
from app.domain.stop.entities.entities import Stop


class StopDbGateway(Protocol):
    async def fetchByVisitId(self, visitId: str) -> List[Stop]:
        ...

    async def beginStop(self, stopId: str):
        ...

    async def completeStop(self, stopId: str):
        ...

    async def beginInspection(self, stopId: str):
        ...

    async def completeInspection(self, stopId: str):
        ...
