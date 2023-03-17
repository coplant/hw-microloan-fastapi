"""add: user-passport

Revision ID: 49b1b268b9f9
Revises: 8f08edbafcbe
Create Date: 2023-03-15 19:21:50.653116

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '49b1b268b9f9'
down_revision = '8f08edbafcbe'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('passport', sa.String(length=1024), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'passport')
    # ### end Alembic commands ###
