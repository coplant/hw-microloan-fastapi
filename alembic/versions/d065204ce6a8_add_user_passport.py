"""add: user-passport

Revision ID: d065204ce6a8
Revises: 49b1b268b9f9
Create Date: 2023-03-15 19:22:56.624390

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'd065204ce6a8'
down_revision = '49b1b268b9f9'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('hashed_passport', sa.String(length=1024), nullable=False))
    op.drop_column('user', 'passport')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('passport', sa.VARCHAR(length=1024), autoincrement=False, nullable=False))
    op.drop_column('user', 'hashed_passport')
    # ### end Alembic commands ###
