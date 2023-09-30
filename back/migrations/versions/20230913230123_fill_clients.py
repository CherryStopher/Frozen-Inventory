"""fill_clients

Revision ID: 66ab5ca26ff9
Revises: ad4d087ddf4f
Create Date: 2023-09-13 23:01:23.209450

"""
import json
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "66ab5ca26ff9"
down_revision: Union[str, None] = "ad4d087ddf4f"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


clients = sa.table(
    "clients",
    sa.Column("rut", sa.String(200), nullable=False),
    sa.Column("name", sa.String(200), nullable=False),
    sa.Column("nickname", sa.String(200), nullable=False),
    sa.Column("phone", sa.String(200), nullable=False),
    sa.Column("email", sa.String(200), nullable=False),
    sa.Column("address", sa.String(200), nullable=False),
    sa.Column("commune", sa.String(200), nullable=False),
)


def upgrade() -> None:
    clients_data = json.load(
        open("migrations/seeds/clients.json", encoding="utf-8-sig")
    )
    op.bulk_insert(clients, clients_data)


def downgrade() -> None:
    op.execute("DELETE FROM clients")
