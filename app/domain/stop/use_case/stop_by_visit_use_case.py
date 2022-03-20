from typing import List
from uuid import uuid4
from datetime import datetime
from app.domain.shared.entities.exceptions import HoumerNotFoundError
from app.domain.stop.entities.entities import Stop
from app.config.container import get_dependencies

houmer_db_gateway = get_dependencies().houmer_db_gateway
stop_db_gateway = get_dependencies().stop_db_gateway


async def fetchByVisitId(visitId:int, houmerId: int) -> List[Stop]:
    houmer = await houmer_db_gateway.fetchById(houmerId)
    if not houmer:
        raise HoumerNotFoundError(houmerId)
    stops = await stop_db_gateway.fetchByVisitId(visitId)
    return stops
