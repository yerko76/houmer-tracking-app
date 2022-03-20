from typing import List
from uuid import uuid4
from datetime import datetime
from app.domain.shared.entities.exceptions import HoumerNotFoundError
from app.domain.shared.entities.shared_entities import Place
from app.domain.stop.entities.entities import Stop, StopEnum
from app.ports.rest.routers.visits.dto.entities import VisitRequest
from app.config.container import get_dependencies
from app.domain.visit.entities.entities import Visit 

houmer_db_gateway = get_dependencies().houmer_db_gateway
places_db_gateway = get_dependencies().place_db_gateway
visit_db_gateway = get_dependencies().visit_db_gateway


def buildStops(places: List[Place]) -> List[Stop]:
    stops = []
    for place in places:
        stop = Stop()
        stop.stopId = str(uuid4())
        stop.description = place.address
        stop.place = place
        stop.status = StopEnum.NOT_STARTED
        stop.start = None
        stop.end = None
        stop.visiting_start = None
        stop.visiting_end = None
        stops.append(stop)
    return stops


async def schedule(houmerId: int, request: VisitRequest) -> Visit:
    houmer = await houmer_db_gateway.fetchById(houmerId)
    if not houmer:
        raise HoumerNotFoundError(houmerId)
    places = await places_db_gateway.fetchByPlaceIds(request.places)

    visit = Visit()
    visit.houmer = houmer
    visit.stops = buildStops(places)
    visit.visitId = str(uuid4())
    visit.cretedAt = datetime.now()
    visit.scheduledAt = datetime.now()
    await visit_db_gateway.save(visit)
    return visit
