"""Initial migration

Revision ID: 8be29ae95318
Revises: 
Create Date: 2025-07-23 15:32:30.202751

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8be29ae95318'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('booking',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('full_name', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('phone', sa.String(length=20), nullable=False),
    sa.Column('event_type', sa.String(length=50), nullable=False),
    sa.Column('event_date', sa.String(length=20), nullable=False),
    sa.Column('event_time', sa.String(length=20), nullable=False),
    sa.Column('guests', sa.Integer(), nullable=False),
    sa.Column('budget', sa.String(length=50), nullable=False),
    sa.Column('notes', sa.Text(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('booking')
    # ### end Alembic commands ###
