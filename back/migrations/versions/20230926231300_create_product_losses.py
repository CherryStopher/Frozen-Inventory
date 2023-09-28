"""create-product-losses

Revision ID: 0cc30ac95ea4
Revises: 11ffbb3f61be
Create Date: 2023-09-26 23:13:00.367173

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "0cc30ac95ea4"
down_revision: Union[str, None] = "11ffbb3f61be"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "product_losses",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("product_id", sa.Integer, sa.ForeignKey("products.id")),
        sa.Column("quantity", sa.Integer, nullable=False),
        sa.Column("enabled", sa.Boolean, default=True),
    )


def downgrade() -> None:
    op.drop_table("product_losses")
