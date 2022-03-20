from typing import List
from uuid import uuid4
from datetime import datetime
from app.config.container import get_dependencies
from app.domain.shared.entities.exceptions import HoumerNotFoundError
from app.domain.shared.entities.shared_entities import Location
from app.domain.visit.entities.entities import Visit
from app.domain.visit.entities.exceptions import VisitNotFoundError
from app.ports.rest.routers.visits.dto.entities import UpdateLocation

houmer_db_gateway = get_dependencies().houmer_db_gateway
visit_db_gateway = get_dependencies().visit_db_gateway


async def updateLocation(houmerId: int, visitId: str, req: UpdateLocation):
    houmer = await houmer_db_gateway.fetchById(houmerId)
    if not houmer:
        raise HoumerNotFoundError(houmerId)
    visitCount = await visit_db_gateway.fetchById(visitId)
    if visitCount == 0:
        raise VisitNotFoundError(visitId)
    location = Location(req.currentLocation.latitude, req.currentLocation.longitude)
    await visit_db_gateway.updateLocation(visitId, location)
