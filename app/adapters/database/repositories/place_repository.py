from typing import Optional, List

from app.domain.shared.entities.shared_entities import Place, Location
from app.adapters.database.models.place import PlaceEntity as Model
from app.adapters.database.configuration.sqlalchemy import database


async def fetchByPlaceIds(placeIds: List[Place]) -> Optional[List[Place]]:
    ids: List[int] = []
    for place in placeIds:
        ids.append(place.placeId)
    query = Model.select().where(Model.c.place_id.in_(ids))
    result = await database.fetch_all(query)

    if result is None:
        return []
    places: List[Place] = []

    for row in result:
        place = Place()
        placeIdTuple = row['place_id']
        place.placeId = placeIdTuple
        place.address = row['address']
        place.location = Location(
            latitude=row['latitude'], longitude=row['longitude'])
        places.append(place)
    return places

async def fetchByPlaceId(placeId: int) -> Place:
    query = Model.select().where(Model.c.place_id == placeId)
    row = await database.fetch_one(query)
    place = Place()
    placeIdTuple = row['place_id']
    place.placeId = placeIdTuple
    place.address = row['address']
    place.location = Location(
        latitude=row['latitude'], longitude=row['longitude'])
    return place
