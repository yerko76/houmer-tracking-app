from typing import Optional, Protocol, List

from app.domain.shared.entities.shared_entities import Place


class PlaceDbGateway(Protocol):
    async def fetchByPlaceIds(self, placeIds: List[Place]) -> Optional[List[Place]]:
        ...
