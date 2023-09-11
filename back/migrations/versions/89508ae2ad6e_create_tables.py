"""create tables

Revision ID: 89508ae2ad6e
Revises: 
Create Date: 2023-09-10 19:29:50.344871

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '89508ae2ad6e'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'supplier',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('fantasy_name', sa.String(100), nullable=False),
        sa.Column('rut', sa.String(100), nullable=False),
        sa.Column('business_name', sa.String(100), nullable=False),
        sa.Column('contact_name', sa.String(100), nullable=False),
        sa.Column('phone', sa.String(100), nullable=False),
        sa.Column('email', sa.String(100), nullable=False),
        sa.Column('retirement_address', sa.String(100), nullable=False),
        sa.Column('payment_method', sa.String(100), nullable=False),
        sa.Column('payment_time', sa.String(100), nullable=False),
    )
    op.create_table(
        'product',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(100), nullable=False),
        sa.Column('barcode', sa.String(100), nullable=False),
        sa.Column('category', sa.String(100), nullable=False),
        sa.Column('supplier_id', sa.Integer, sa.ForeignKey('supplier.id')),
        sa.Column('measurement_unit', sa.String(100), nullable=False),
        sa.Column('measurement_unit_quantity', sa.Integer, nullable=False),
        sa.Column('base', sa.String(100), nullable=False),
    )


def downgrade() -> None:
    op.drop_table('product')
    op.drop_table('supplier')
