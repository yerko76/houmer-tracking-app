import logging
from typing import Any, Dict, Iterable

from databases import Database
from sqlalchemy.schema import Table

from app.adapters.database.models.houmer import HoumerEntity
from app.adapters.database.models.place import PlaceEntity
from app.adapters.database.configuration.sqlalchemy import (
    database_context,
    init_database
)

logger = logging.getLogger(__name__)


async def _populate_table(
    db: Database, table: Table, values: Iterable[Dict[str, Any]],
):
    name: str = table.name
    query = table.insert()

    logger.info(f"Seeding table {name}")
    await db.execute_many(query, list(values))
    logger.info(f"Seeded table {name} successfully")


async def _populate_tables(db: Database) -> None:
    houmers = [
        {"first_name": "john", "last_name": "doe",
            "email": "john@example", "phone_number": "333333"},
        {"first_name": "juan", "last_name": "perez",
            "email": "juan@example", "phone_number": "444444"},
        {"first_name": "ana", "last_name": "contreras",
            "email": "ana@example", "phone_number": "555555"},
        {"first_name": "armando", "last_name": "casas",
            "email": "armando@example", "phone_number": "999999"},
        {"first_name": "daniela", "last_name": "castro",
            "email": "daniela@example", "phone_number": "888888"},
        {"first_name": "sofia", "last_name": "gomez",
            "email": "sofia@example", "phone_number": "777777"}
    ]
    await _populate_table(db, HoumerEntity, houmers)
    places = [{"address": "Irarrázaval 4200, Ñuñoa", "longitude": -
               33.455131614036866, "latitude": -70.58640357148082},
              {"address": "Av. Providencia 153, Providencia", "longitude":
               -33.43637431285144, "latitude": -70.63164251872415},
              ]
    await _populate_table(db, PlaceEntity, places)


async def run() -> None:
    logger.info("Initializing databases")
    init_database()
    async with database_context() as database:
        logger.info("Populating database")
        for fn in [_populate_tables]:
            await fn(database)
        logger.info("Finished populating PostgreSQL database")
