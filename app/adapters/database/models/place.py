from sqlalchemy.schema import Column, Table
from sqlalchemy.types import Integer, Float, Text

from app.adapters.database.configuration.sqlalchemy import metadata

PlaceEntity = Table(
    "place",
    metadata,
    Column("place_id", Integer, primary_key=True, autoincrement=True),
    Column("address", Text(), nullable=False),
    Column("latitude", Float, nullable=False),
    Column("longitude", Float, nullable=False),
)
