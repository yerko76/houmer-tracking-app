from typing import Optional

from app.domain.shared.entities.shared_entities import Houmer
from app.adapters.database.models.houmer import HoumerEntity as Model
from app.adapters.database.configuration.sqlalchemy import database


async def fetchById(houmerId: int) -> Optional[Houmer]:
    query = Model.select().where(Model.c.houmer_id == houmerId)
    result = await database.fetch_one(query)
    if result is None:
        return None
    houmerRecord = dict(result.items())
    houmer = Houmer()
    houmer.houmerId = houmerRecord['houmer_id']
    houmer.firstName = houmerRecord['first_name']
    houmer.lastName = houmerRecord['last_name']
    houmer.email = houmerRecord['email']
    houmer.phoneNumber = houmerRecord['phone_number']
    return houmer
