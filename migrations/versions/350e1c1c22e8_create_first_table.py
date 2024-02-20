"""Create first table

Revision ID: 350e1c1c22e8
Revises: e6cb8fe731e4
Create Date: 2024-02-20 01:00:53.502336

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '350e1c1c22e8'
down_revision = 'e6cb8fe731e4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('buttons',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('buttons')
    # ### end Alembic commands ###
