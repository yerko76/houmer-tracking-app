"""create stop table

Revision ID: ef2d1c560690
Revises: 940759406b54
Create Date: 2022-03-18 00:58:23.146674

"""
from alembic import op
import sqlalchemy as sa
import uuid
from sqlalchemy.dialects.postgresql import UUID


# revision identifiers, used by Alembic.
revision = "ef2d1c560690"
down_revision = "940759406b54"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "stop",
        sa.Column("stop_id", UUID(as_uuid=True), nullable=False,
                  primary_key=True, default=uuid.uuid4),
        sa.Column("status", sa.TEXT(), nullable=False),
        sa.Column("start_at", sa.DateTime(), nullable=True),
        sa.Column("end_at", sa.DateTime(), nullable=True),
        sa.Column("visiting_start", sa.DateTime(), nullable=True),
        sa.Column("visiting_end", sa.DateTime(), nullable=True),
        sa.Column("place_id", sa.Integer(), nullable=False),
        sa.Column("visit_id", UUID(as_uuid=True), nullable=False),
        sa.ForeignKeyConstraint(('place_id',), ['place.place_id'],),
        sa.ForeignKeyConstraint(('visit_id',), ['visit.visit_id'],),
    )


def downgrade():
    op.drop_table("stop")
