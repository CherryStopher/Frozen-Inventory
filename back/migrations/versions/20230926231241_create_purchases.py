"""create-purchases

Revision ID: 097c5419bf68
Revises: 790cdc6252f0
Create Date: 2023-09-26 23:12:41.794822

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "097c5419bf68"
down_revision: Union[str, None] = "790cdc6252f0"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "purchases",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("supplier_id", sa.Integer, sa.ForeignKey("suppliers.id")),
        sa.Column("date", sa.DateTime),
        sa.Column("enabled", sa.Boolean, default=True),
    )


def downgrade() -> None:
    op.drop_table("purchases")
