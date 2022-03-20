"""Creates houmer table

Revision ID: ddcee6b6460d
Revises: 
Create Date: 2022-03-16 18:55:59.800982

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "ddcee6b6460d"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "houmer",
        sa.Column("houmer_id", sa.Integer(), nullable=False, autoincrement=True),
        sa.Column("first_name", sa.Text(), nullable=False),
        sa.Column("last_name", sa.Text(), nullable=False),
        sa.Column("email", sa.Text(), nullable=False),
        sa.Column("phone_number", sa.Text(), nullable=False),
        sa.PrimaryKeyConstraint("houmer_id", name=op.f("pk_houmer")),
        sa.UniqueConstraint("email", name=op.f("uq_user_email")),
    )


def downgrade():
    op.drop_table("houmer")
