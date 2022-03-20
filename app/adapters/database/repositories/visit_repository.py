from app.domain.stop.entities.entities import StopEnum
from app.domain.visit.entities.entities import Visit
from app.adapters.database.models.visit import VisitEntity
from app.domain.visit.entities.entities import Location
from app.adapters.database.models.stop import StopEntity
from app.adapters.database.configuration.sqlalchemy import database
from datetime import datetime
import uuid


@database.transaction()
async def save(visit: Visit):
    values = {'visit_id': visit.visitId,
              'houmer_id': visit.houmer.houmerId,
              'scheduled_at': visit.scheduledAt, 'created_at': datetime.now()}
    visitQuery = VisitEntity.insert().values(values)
    await database.execute(visitQuery)

    for stop in visit.stops:
        values = {"stop_id": stop.stopId, "status": StopEnum.NOT_STARTED.value,
                  "place_id": stop.place.placeId, "visit_id": visit.visitId
                  }
        stopQuery = StopEntity.insert().values(values)
        await database.execute(stopQuery)


@database.transaction()
async def updateLocation(visitId: str, location: Location):
    visitIdUUid = uuid.UUID(visitId).hex
    values = {'houmer_long': location.longitude, "houmer_lat": location.latitude, }
    query = VisitEntity.update().values(values).where(VisitEntity.c.visit_id == visitIdUUid)
    await database.execute(query)


async def fetchById(visitId: str) -> Visit:
    visitIdUUid = uuid.UUID(visitId).hex
    query = VisitEntity.count().where(VisitEntity.c.visit_id == visitIdUUid)
    result = await database.fetch_one(query)
    return result[0]
