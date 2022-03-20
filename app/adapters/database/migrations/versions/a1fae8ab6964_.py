"""Creates places table

Revision ID: a1fae8ab6964
Revises: ddcee6b6460d
Create Date: 2022-03-16 19:41:40.992898

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "a1fae8ab6964"
down_revision = "ddcee6b6460d"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "place",
        sa.Column("place_id", sa.Integer(), nullable=False, autoincrement=True),
        sa.Column("address", sa.Text(), nullable=False),
        sa.Column("longitude", sa.Float(), nullable=False),
        sa.Column("latitude", sa.Float(), nullable=False),
        sa.PrimaryKeyConstraint("place_id", name=op.f("pk_place")),
    )


def downgrade():
    op.drop_table("place")
