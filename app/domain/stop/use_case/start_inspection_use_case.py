from app.config.container import get_dependencies
from app.domain.shared.entities.exceptions import HoumerNotFoundError

stop_db_gateway = get_dependencies().stop_db_gateway
houmer_db_gateway = get_dependencies().houmer_db_gateway


async def startInspection(houmerId: int, stopId: str):
    houmer = await houmer_db_gateway.fetchById(houmerId)
    if not houmer:
        raise HoumerNotFoundError(houmerId)
    await stop_db_gateway.beginInspection(stopId)
