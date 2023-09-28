"""create_suppliers

Revision ID: e0d92bfecd7a
Revises:
Create Date: 2023-09-13 22:57:00.209563

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "e0d92bfecd7a"
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


def downgrade() -> None:
    op.drop_table("suppliers")
