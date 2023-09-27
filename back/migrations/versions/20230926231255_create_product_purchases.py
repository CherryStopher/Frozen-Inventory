"""create-product-purchases

Revision ID: 11ffbb3f61be
Revises: 1d2edfafacc2
Create Date: 2023-09-26 23:12:55.280554

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "11ffbb3f61be"
down_revision: Union[str, None] = "1d2edfafacc2"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "product_purchases",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("purchase_id", sa.Integer, sa.ForeignKey("purchases.id")),
        sa.Column("product_id", sa.Integer, sa.ForeignKey("products.id")),
        sa.Column("quantity", sa.Integer, nullable=False),
        sa.Column("unit_price", sa.Integer, nullable=False),
    )


def downgrade() -> None:
    op.drop_table("product_purchases")
