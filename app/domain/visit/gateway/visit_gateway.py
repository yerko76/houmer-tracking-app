from typing import Protocol, Optional

from app.domain.visit.entities.entities import Visit
from app.domain.visit.entities.entities import Location


class VisitDbGateway(Protocol):
    async def save(self, visit: Visit):
        ...

    async def fetchById(self, visitId: str) -> Optional[Visit]:
        ...

    async def updateLocation(self, visitId: str, location: Location):
        ...
