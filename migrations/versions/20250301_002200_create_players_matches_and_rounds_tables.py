"""create players, matches, and rounds tables

Revision ID: 170405ff7bb6
Revises: 
Create Date: 2025-03-01 00:22:00.919028

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '170405ff7bb6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('players',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('strategy', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('matches',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('match_num', sa.Integer(), nullable=True),
    sa.Column('player1', sa.Integer(), nullable=True),
    sa.Column('player2', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['player1'], ['players.id'], ),
    sa.ForeignKeyConstraint(['player2'], ['players.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('rounds',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('round', sa.Integer(), nullable=False),
    sa.Column('move1', sa.String(length=1), nullable=False),
    sa.Column('move2', sa.String(length=1), nullable=False),
    sa.Column('match_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['match_id'], ['matches.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('rounds')
    op.drop_table('matches')
    op.drop_table('players')
    # ### end Alembic commands ###
