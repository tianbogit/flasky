"""eidt role model

Revision ID: 130c74458e30
Revises: f2cc4d27b100
Create Date: 2018-11-06 13:20:59.385308

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '130c74458e30'
down_revision = 'f2cc4d27b100'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('role_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'users', 'roles', ['role_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.drop_column('users', 'role_id')
    # ### end Alembic commands ###