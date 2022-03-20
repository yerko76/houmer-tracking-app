from typing import Optional, Protocol

from app.domain.shared.entities.shared_entities import Houmer


class HoumerDbGateway(Protocol):
    async def fetchById(self, houmerId: int) -> Optional[Houmer]:
        ...
