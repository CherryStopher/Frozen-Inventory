"""create-products

Revision ID: 7deda965c06c
Revises: 66ab5ca26ff9
Create Date: 2023-09-26 22:51:08.690524

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "7deda965c06c"
down_revision: Union[str, None] = "66ab5ca26ff9"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "products",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("name", sa.String(200), nullable=False),
        sa.Column("supplier_id", sa.Integer, sa.ForeignKey("suppliers.id")),
        sa.Column("barcode", sa.String(200), nullable=False),
        sa.Column("category", sa.String(200), nullable=False),
        sa.Column("measurement_unit", sa.String(200), nullable=False),
        sa.Column("measurement_unit_quantity", sa.Integer, nullable=False),
        sa.Column("current_price", sa.Float, nullable=False),
    )


def downgrade() -> None:
    op.drop_table("products")
