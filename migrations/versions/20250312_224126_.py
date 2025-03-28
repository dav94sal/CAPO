"""empty message

Revision ID: 71e68415cb7c
Revises: 46613040f586
Create Date: 2025-03-12 22:41:26.210509

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '71e68415cb7c'
down_revision = '46613040f586'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('matches', schema=None) as batch_op:
        batch_op.add_column(sa.Column('createdAt', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True))
        batch_op.alter_column('match_num',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('tournament_num',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('player1',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('player2',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('matches', schema=None) as batch_op:
        batch_op.alter_column('player2',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('player1',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('tournament_num',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('match_num',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.drop_column('createdAt')

    # ### end Alembic commands ###
