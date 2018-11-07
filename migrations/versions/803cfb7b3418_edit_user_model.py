"""edit user model

Revision ID: 803cfb7b3418
Revises: c3fe8cc9cb49
Create Date: 2018-11-07 11:12:24.533292

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '803cfb7b3418'
down_revision = 'c3fe8cc9cb49'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('avatar_hash', sa.String(length=32), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'avatar_hash')
    # ### end Alembic commands ###
