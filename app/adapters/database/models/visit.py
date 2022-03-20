from sqlalchemy.schema import Column, Table, ForeignKey
from sqlalchemy.types import Integer, Float,  Date, DateTime
from sqlalchemy.dialects.postgresql import UUID
import uuid

from app.adapters.database.configuration.sqlalchemy import metadata

VisitEntity = Table(
    "visit",
    metadata,
    Column("visit_id", UUID(), primary_key=True, default=uuid.uuid4),
    Column("houmer_id", Integer, ForeignKey(
        "houmer.houmer_id"), index=True, nullable=False),
    Column("scheduled_at", Date(), nullable=False),
    Column("created_at", DateTime(), nullable=False),
    Column("houmer_long", Float(), nullable=True),
    Column("houmer_lat", Float(), nullable=True),
)
