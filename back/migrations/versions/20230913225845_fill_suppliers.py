"""fill_suppliers

Revision ID: d3f46729a8da
Revises: e0d92bfecd7a
Create Date: 2023-09-13 22:58:45.084048

"""
import json
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "d3f46729a8da"
down_revision: Union[str, None] = "e0d92bfecd7a"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

suppliers = sa.table(
    "suppliers",
    sa.Column("fantasy_name", sa.String(100), nullable=True),
    sa.Column("rut", sa.String(100), nullable=False),
    sa.Column("business_name", sa.String(100), nullable=False),
    sa.Column("contact_name", sa.String(100), nullable=True),
    sa.Column("phone", sa.String(100), nullable=True),
    sa.Column("email", sa.String(100), nullable=True),
)


def upgrade() -> None:
    suppliers_data = json.load(open("migrations/seeds/suppliers.json"))
    op.bulk_insert(suppliers, suppliers_data)


def downgrade() -> None:
    op.execute("DELETE FROM suppliers")
