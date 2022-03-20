from app.domain.stop.entities.entities import Stop, StopEnum
from app.adapters.database.models.stop import StopEntity
from app.adapters.database.repositories import place_repository
from app.adapters.database.configuration.sqlalchemy import database
from typing import List
from datetime import datetime
import uuid


async def fetchByVisitId(visitId: str) -> List[Stop]:
    visitIdUUid = uuid.UUID(visitId).hex
    query = StopEntity.select().where(StopEntity.c.visit_id == visitIdUUid)
    result = await database.fetch_all(query)
    if result is None:
        return []
    stops: List[Stop] = []
    # refactor this multiple querys (check orm to load relationships)
    for row in result:
        placeIdTuple = row['place_id']
        place = await place_repository.fetchByPlaceId(placeIdTuple)
        stop = Stop()
        stop.stopId = str(row['stop_id'])
        stop.status = row['status']
        stop.start = row['start_at']
        stop.end = row['end_at']
        stop.visitingStart = row['visiting_start']
        stop.visitingEnd = row['visiting_end']
        stop.place = place
        stops.append(stop)
    return stops


async def beginStop(stopId: str):
    values = {"start_at": datetime.now(), "status": StopEnum.IN_PROGRESS.value}
    query = (
        StopEntity.update()
        .where(StopEntity.c.stop_id == stopId)
        .where(StopEntity.c.status == "NOT_STARTED")
        .values(values)
    )
    await database.execute(query)


async def completeStop(stopId: str):
    values = {"end_at": datetime.now(), "status": StopEnum.ARRIVED_TO_LOCATION.value}
    query = (
        StopEntity.update()
        .where(StopEntity.c.stop_id == stopId)
        .where(StopEntity.c.status == "IN_PROGRESS")
        .values(values)
    )
    await database.execute(query)


async def beginInspection(stopId: str):
    values = {"visiting_start": datetime.now(), "status": StopEnum.VISITING.value}
    query = (
        StopEntity.update()
        .where(StopEntity.c.stop_id == stopId)
        .where(StopEntity.c.status != "COMPLETED")
        .values(values)
    )
    await database.execute(query)


async def completeInspection(stopId: str):
    values = {"visiting_end": datetime.now(), "status": StopEnum.COMPLETED.value}
    query = (
        StopEntity.update()
        .where(StopEntity.c.stop_id == stopId)
        .where(StopEntity.c.status == "VISITING")
        .values(values)
    )
    await database.execute(query)
