"""Удалил таблицу complete_task

Revision ID: ddc049ec4877
Revises: 3d467a1236f6
Create Date: 2024-02-22 00:20:44.872576

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ddc049ec4877'
down_revision = '3d467a1236f6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('complete_task')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('complete_task',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('task_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('done', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['task_id'], ['tasks.id'], name='complete_task_task_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='complete_task_pkey')
    )
    # ### end Alembic commands ###
