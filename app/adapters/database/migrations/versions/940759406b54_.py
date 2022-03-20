"""create table visit

Revision ID: 940759406b54
Revises: a1fae8ab6964
Create Date: 2022-03-17 19:09:13.917286

"""
from alembic import op
import sqlalchemy as sa
import uuid
from sqlalchemy.dialects.postgresql import UUID

# revision identifiers, used by Alembic.
revision = "940759406b54"
down_revision = "a1fae8ab6964"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "visit",
        sa.Column("visit_id", UUID(as_uuid=True), nullable=False,
                  primary_key=True, default=uuid.uuid4),
        sa.Column("houmer_id", sa.Integer(), nullable=False),
        sa.Column("scheduled_at", sa.Date(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("houmer_long", sa.Float(), nullable=True),
        sa.Column("houmer_lat", sa.Float(), nullable=True),
        sa.ForeignKeyConstraint(['houmer_id'], ['houmer.houmer_id'])
    )


def downgrade():
    op.drop_table("visit")
