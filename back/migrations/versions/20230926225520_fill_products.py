"""fill-products

Revision ID: 790cdc6252f0
Revises: 7deda965c06c
Create Date: 2023-09-26 22:55:20.563791

"""
import json
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "790cdc6252f0"
down_revision: Union[str, None] = "7deda965c06c"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

products = sa.table(
    "products",
    sa.Column("name", sa.String(200), nullable=False),
    sa.Column("supplier_id", sa.Integer, sa.ForeignKey("suppliers.id")),
    sa.Column("barcode", sa.String(200), nullable=False),
    sa.Column("category", sa.String(200), nullable=False),
    sa.Column("measurement_unit", sa.String(200), nullable=False),
    sa.Column("measurement_unit_quantity", sa.Integer, nullable=False),
    sa.Column("current_price", sa.Float, nullable=False),
)


def upgrade() -> None:
    products_data = json.load(open("migrations/seeds/products.json", encoding='utf-8-sig'))
    conn = op.get_bind()
    suppliers = conn.execute(sa.text("SELECT id, business_name FROM suppliers")).fetchall()
    suppliers_dict = {supplier.business_name: supplier.id for supplier in suppliers}
    for product in products_data:
        product["supplier_id"] = suppliers_dict[product["supplier"]]
    op.bulk_insert(products, products_data)


def downgrade() -> None:
    op.execute("DELETE FROM products")
