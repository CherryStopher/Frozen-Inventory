"""create_clients

Revision ID: ad4d087ddf4f
Revises: d3f46729a8da
Create Date: 2023-09-13 23:00:39.826279

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "ad4d087ddf4f"
down_revision: Union[str, None] = "d3f46729a8da"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "clients",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("rut", sa.String(200), nullable=False),
        sa.Column("name", sa.String(200), nullable=False),
        sa.Column("nickname", sa.String(200), nullable=False),
        sa.Column("phone", sa.String(200), nullable=False),
        sa.Column("email", sa.String(200), nullable=False),
        sa.Column("address", sa.String(200), nullable=False),
        sa.Column("commune", sa.String(200), nullable=False),
    )


def downgrade() -> None:
    op.drop_table("clients")
