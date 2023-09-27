"""create-movements

Revision ID: ba058b61fc94
Revises: e165ef28b911
Create Date: 2023-09-26 23:13:10.846220

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "ba058b61fc94"
down_revision: Union[str, None] = "e165ef28b911"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
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
