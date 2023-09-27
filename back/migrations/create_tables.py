"""create tables

Revision ID: 89508ae2ad6e
Revises: 
Create Date: 2023-09-10 19:29:50.344871

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "89508ae2ad6e"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "suppliers",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("fantasy_name", sa.String(100), nullable=True),
        sa.Column("rut", sa.String(100), nullable=False),
        sa.Column("business_name", sa.String(100), nullable=False),
        sa.Column("contact_name", sa.String(100), nullable=True),
        sa.Column("phone", sa.String(100), nullable=True),
        sa.Column("email", sa.String(100), nullable=True),
    )

    op.create_table(
        "clients",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("fantasy_name", sa.String(100), nullable=False),
        sa.Column("rut", sa.String(200), nullable=False),
        sa.Column("business_name", sa.String(200), nullable=False),
        sa.Column("nickname", sa.String(200), nullable=False),
        sa.Column("contact_name", sa.String(200), nullable=False),
        sa.Column("phone", sa.String(200), nullable=False),
        sa.Column("email", sa.String(200), nullable=False),
        sa.Column("address", sa.String(200), nullable=False),
        sa.Column("commune", sa.String(200), nullable=False),
    )

    op.create_table(
        "purchases",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("supplier_id", sa.Integer, sa.ForeignKey("suppliers.id")),
        sa.Column("date", sa.DateTime),
        sa.Column("enabled", sa.Boolean, default=True),
    )

    op.create_table(
        "products",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(100), nullable=False),
        sa.Column("barcode", sa.String(100), nullable=False),
        sa.Column("category", sa.String(100), nullable=False),
        sa.Column("supplier_id", sa.Integer, sa.ForeignKey("suppliers.id")),
        sa.Column("measurement_unit", sa.String(100), nullable=False),
        sa.Column("measurement_unit_quantity", sa.Integer, nullable=False),
        sa.Column("base", sa.String(100), nullable=False),
    )

    op.create_table(
        "sales",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("client_id", sa.Integer, sa.ForeignKey("clients.id")),
        sa.Column("date", sa.DateTime),
        sa.Column("enabled", sa.Boolean, default=True),
    )

    op.create_table(
        "product_purchases",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("purchase_id", sa.Integer, sa.ForeignKey("purchases.id")),
        sa.Column("product_id", sa.Integer, sa.ForeignKey("products.id")),
        sa.Column("quantity", sa.Integer, nullable=False),
        sa.Column("unit_price", sa.Integer, nullable=False),
    )

    op.create_table(
        "product_losses",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("product_id", sa.Integer, sa.ForeignKey("products.id")),
        sa.Column("quantity", sa.Integer, nullable=False),
        sa.Column("enabled", sa.Boolean, default=True),
    )

    op.create_table(
        "product_sales",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("product_id", sa.Integer, sa.ForeignKey("products.id")),
        sa.Column("sale_id", sa.Integer, sa.ForeignKey("sales.id")),
        sa.Column("quantity", sa.Integer, nullable=False),
        sa.Column("unit_price", sa.Integer, nullable=False),
    )

    op.create_table(
        "movements",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("product_id", sa.Integer, sa.ForeignKey("products.id")),
        sa.Column(
            "product_purchase_id", sa.Integer, sa.ForeignKey("product_purchases.id")
        ),
        sa.Column("product_loss_id", sa.Integer, sa.ForeignKey("product_losses.id")),
        sa.Column("product_sale_id", sa.Integer, sa.ForeignKey("product_sales.id")),
        sa.Column("location", sa.String(100), nullable=False),
        sa.Column("quantity", sa.Integer, nullable=False),
        sa.Column("balance", sa.Integer, nullable=False),
        sa.Column("description", sa.String(100), nullable=False),
    )


def downgrade() -> None:
    op.drop_table("movements")
    op.drop_table("product_purchases")
    op.drop_table("product_losses")
    op.drop_table("product_sales")
    op.drop_table("sales")
    op.drop_table("purchases")
    op.drop_table("products")
    op.drop_table("suppliers")
    op.drop_table("clients")
