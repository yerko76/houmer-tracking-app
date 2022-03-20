from typing import List
from app.ports.rest.routers.visits.dto.entities import VisitRequest, VisitResponse, Location, UpdateLocation, Stop as StopDTO
from app.domain.visit.usecase import schedule_visit_usecase, update_houmer_location
from fastapi.routing import APIRouter

router = APIRouter()


@router.post(
    "/houmer/{houmerId}",
    status_code=201,
    tags=["visit"],
    summary="Schedule visit",
    description="Schedule visit for existing houmer and existing places",
    responses={
        201: {"description": "Schedule a visit"},
        401: {"description": "User unauthorized"},
    },
)
async def scheduleVisit(houmerId: int, request: VisitRequest) -> VisitResponse:
    visit = await schedule_visit_usecase.schedule(houmerId, request)
    stopDtos: List[StopDTO] = []
    for stop in visit.stops:
        stopDto = StopDTO(stopId=stop.stopId, description=stop.description,
                          placeId=stop.place.placeId,
                          location=Location(longitude=stop.place.location.longitude, latitude=stop.place.location.latitude))
        stopDtos.append(stopDto)
    return VisitResponse(visitId=visit.visitId, stops=stopDtos)


@router.put(
    "{visitId}/houmer/{houmerId}",
    status_code=201,
    tags=["visit"],
    summary="Update houmer location",
    description="Updates houmer location by given visit",
    responses={
        201: {"description": "Updated location"},
        401: {"description": "User unauthorized"},
    },
)
async def updateLocation(visitId: str, houmerId: int, request: UpdateLocation):
    await update_houmer_location.updateLocation(houmerId, visitId, request)
    return {"message": "houmer location updated"}