from typing import List
from datetime import date
from app.domain.stop.use_case import stop_by_visit_use_case
from app.domain.stop.use_case import begin_stop_use_case
from app.domain.stop.use_case import complete_stop_use_case
from app.domain.stop.use_case import start_inspection_use_case
from app.domain.stop.use_case import complete_inspection_use_case
from app.domain.stop.use_case import stops_by_date_use_case

from app.ports.rest.routers.visits.dto.entities import Stop as StopDto
from app.ports.rest.routers.visits.dto.entities import StopResponse
from app.ports.rest.routers.visits.dto.entities import Location
from fastapi.routing import APIRouter

router = APIRouter()


@router.get(
    "/{visitId}/houmer/{houmerId}/stops",
    status_code=200,
    tags=["stops"],
    summary="get stops by given visitId",
    description="Returns stops associated to a visitId",
)
async def getStopsByVisit(visitId: str, houmerId: int) -> List[StopDto]:
    stops = await stop_by_visit_use_case.fetchByVisitId(visitId, houmerId)
    stopDtos: List[StopDto] = []
    for stop in stops:
        latitude = stop.place.location.latitude
        longitude = stop.place.location.longitude
        stopLocation = Location(latitude=latitude, longitude=longitude)
        stopDto = StopDto(stopId=stop.stopId, placeId=stop.place.placeId,
                          description=stop.place.address, location=stopLocation)
        stopDtos.append(stopDto)
    return stopDtos


@router.put(
    "/houmer/{houmerId}/stops/{stopId}/begin",
    status_code=201,
    tags=["stops"],
    summary="start trip to location",
    description="start trip to the selected location",
)
async def beginStop(houmerId: int, stopId: str):
    await begin_stop_use_case.beginStop(houmerId, stopId)
    return {"message": "started trip to location"}


@router.get(
    "/houmer/{houmerId}/stops",
    status_code=200,
    tags=["stops"],
    summary="Get visited stops by a given date",
    description="Return the stops visited by the houmer by given date"
)
async def stopsByDate(houmerId: int, visitedDay: date) -> List[StopResponse]:
    stops = await stops_by_date_use_case.getStopsByDate(houmerId, visitedDay)
    stopDtos: List[StopResponse] = []
    for stop in stops:
        timeInLocation = stop.visitingEnd - stop.visitingStart
        time = divmod(timeInLocation.seconds, 60)
        formattedTime = f'{time[0]}:minutes, {time[1]}:seconds'
        latitude = stop.place.location.latitude
        longitude = stop.place.location.longitude
        stopLocation = Location(latitude=latitude, longitude=longitude)
        stopDto = StopResponse(stopId=stop.stopId, description=stop.place.address,
                               location=stopLocation, timeInLocation=formattedTime)
        stopDtos.append(stopDto)
    return stopDtos


@router.put(
    "/houmer/{houmerId}/stops/{stopId}/complete",
    status_code=201,
    tags=["stops"],
    summary="Complete trip to location",
    description="Complete trip to given stopId",
)
async def completeStop(houmerId: int, stopId: str):
    await complete_stop_use_case.completeStop(houmerId, stopId)
    return {"message": "completed trip to location"}


@router.put(
    "/houmer/{houmerId}/stops/{stopId}/inspection/start",
    status_code=201,
    tags=["stops"],
    summary="Start the visit/inspection of location",
    description="Start the visit/inspection of location",
)
async def startInspection(houmerId: int, stopId: str):
    await start_inspection_use_case.startInspection(houmerId, stopId)
    return {"message": "started inspection to location"}


@router.put(
    "/houmer/{houmerId}/stops/{stopId}/inspection/complete",
    status_code=201,
    tags=["stops"],
    summary="Complete inspection of location",
    description="Complete inspection of given location",
)
async def completeInspection(houmerId: int, stopId: str):
    await complete_inspection_use_case.completeInspection(houmerId, stopId)
    return {"message": "ended inspection to location"}
