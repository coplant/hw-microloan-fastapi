"""initial

Revision ID: 7fa0528d3495
Revises: 
Create Date: 2023-03-18 03:04:56.651918

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '7fa0528d3495'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('last_name', sa.String(), nullable=False),
                    sa.Column('first_name', sa.String(), nullable=False),
                    sa.Column('middle_name', sa.String(), nullable=False),
                    sa.Column('passport', sa.String(), nullable=False),
                    sa.Column('period', sa.Integer(), nullable=False),
                    sa.Column('amount', sa.Integer(), nullable=False),
                    sa.Column('status', sa.String(), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###