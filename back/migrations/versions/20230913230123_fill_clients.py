"""fill_clients

Revision ID: 66ab5ca26ff9
Revises: ad4d087ddf4f
Create Date: 2023-09-13 23:01:23.209450

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '66ab5ca26ff9'
down_revision: Union[str, None] = 'ad4d087ddf4f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
