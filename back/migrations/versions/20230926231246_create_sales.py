"""create-sales

Revision ID: 1d2edfafacc2
Revises: 097c5419bf68
Create Date: 2023-09-26 23:12:46.906850

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "1d2edfafacc2"
down_revision: Union[str, None] = "097c5419bf68"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "sales",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("client_id", sa.Integer, sa.ForeignKey("clients.id")),
        sa.Column("date", sa.DateTime),
        sa.Column("enabled", sa.Boolean, default=True),
    )


def downgrade() -> None:
    op.drop_table("sales")
