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
    )
    
    op.create_table(
        'client',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('fantasy_name', sa.String(100), nullable=False),
        sa.Column('rut', sa.String(200), nullable=False),
        sa.Column('business_name', sa.String(200), nullable=False),
        sa.Column('nickname', sa.String(200), nullable=False),
        sa.Column('contact_name', sa.String(200), nullable=False),
        sa.Column('phone', sa.String(200), nullable=False),
        sa.Column('email', sa.String(200), nullable=False),
        sa.Column('adress', sa.String(200), nullable=False),
        sa.Column('commune', sa.String(200), nullable=False),
        sa.Column('payment_method', sa.String(200), nullable=False),
    )
    
    op.create_table(
        'purchase',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('supplier_id', sa.Integer, sa.ForeignKey('supplier.id')),
        sa.Column('date', sa.DateTime),
        sa.Column('enabled', sa.Boolean, default=True),
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
    
    op.create_table(
        'sale',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('client_id', sa.Integer, sa.ForeignKey('client.id')),
        sa.Column('date', sa.DateTime),
        sa.Column('enabled', sa.Boolean, default=True),
    )
    
    op.create_table(
        'product_purchase',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('purchase_id', sa.Integer, sa.ForeignKey('purchase.id')),
        sa.Column('product_id', sa.Integer, sa.ForeignKey('product.id')),
        sa.Column('quantity', sa.Integer, nullable=False),
        sa.Column('unit_price', sa.Integer, nullable=False),
    )
    
    op.create_table(
        'product_loss',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('product_id', sa.Integer, sa.ForeignKey('product.id')),
        sa.Column('quantity', sa.Integer, nullable=False),
        sa.Column('enabled', sa.Boolean, default=True),
    )
    
    op.create_table(
        'product_sale',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('product_id', sa.Integer, sa.ForeignKey('product.id')),
        sa.Column('sale_id', sa.Integer, sa.ForeignKey('sale.id')),
        sa.Column('quantity', sa.Integer, nullable=False),
        sa.Column('unit_price', sa.Integer, nullable=False),
    )
    
    op.create_table(
        'movement',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('product_id', sa.Integer, sa.ForeignKey('product.id')),
        sa.Column('product_purchase_id', sa.Integer, sa.ForeignKey('product_purchase.id')),
        sa.Column('product_loss_id', sa.Integer, sa.ForeignKey('product_loss.id')),
        sa.Column('product_sale_id', sa.Integer, sa.ForeignKey('product_sale.id')),
        sa.Column('location', sa.String(100), nullable=False),
        sa.Column('quantity', sa.Integer, nullable=False),
        sa.Column('balance', sa.Integer, nullable=False),
        sa.Column('description', sa.String(100), nullable=False),
    )


def downgrade() -> None:
    op.drop_table('product')
    op.drop_table('supplier')
