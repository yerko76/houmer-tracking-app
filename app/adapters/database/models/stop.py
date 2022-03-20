from sqlalchemy.schema import Column, Table, ForeignKey
from sqlalchemy.types import Integer, Float, Text, DateTime
from sqlalchemy.dialects.postgresql import UUID
import uuid

from app.adapters.database.configuration.sqlalchemy import metadata

StopEntity = Table(
    "stop",
    metadata,
    Column("stop_id", UUID(), primary_key=True, default=uuid.uuid4),
    Column("visit_id", UUID(), ForeignKey(
        "visit.visit_id"), nullable=False, index=True),
    Column("place_id", Integer, ForeignKey(
        "place.place_id"), nullable=False),
    Column("status", Text(), nullable=False, index=True),
    Column("start_at", DateTime(), nullable=True),
    Column("end_at", DateTime(), nullable=True),
    Column("visiting_start", DateTime(), nullable=True),
    Column("visiting_end", DateTime(), nullable=True),
)
