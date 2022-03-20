from sqlalchemy.schema import Column, Table
from sqlalchemy.types import Integer, Text

from app.adapters.database.configuration.sqlalchemy import metadata

HoumerEntity = Table(
    "houmer",
    metadata,
    Column("houmer_id", Integer, primary_key=True, autoincrement=True),
    Column("email", Text(), unique=True, nullable=False),
    Column("first_name", Text(), nullable=False),
    Column("last_name", Text(), nullable=False),
    Column("phone_number", Text(), nullable=False),
)
