"""create-product-sales

Revision ID: e165ef28b911
Revises: 0cc30ac95ea4
Create Date: 2023-09-26 23:13:05.715556

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "e165ef28b911"
down_revision: Union[str, None] = "0cc30ac95ea4"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "product_sales",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("product_id", sa.Integer, sa.ForeignKey("products.id")),
        sa.Column("sale_id", sa.Integer, sa.ForeignKey("sales.id")),
        sa.Column("quantity", sa.Integer, nullable=False),
        sa.Column("unit_price", sa.Integer, nullable=False),
    )


def downgrade() -> None:
    op.drop_table("product_sales")
