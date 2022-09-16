"""empty message

Revision ID: 25a686d8aded
Revises: 56ef2c90e7f5
Create Date: 2022-09-15 09:52:28.281391

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '25a686d8aded'
down_revision = '56ef2c90e7f5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('bet_slip', sa.Column('teamWon', sa.String(length=300), nullable=True))
    op.drop_column('bet_slip', 'team2')
    op.drop_column('bet_slip', 'team1')
    op.drop_column('bet_slip', 'odds2')
    op.drop_column('userBets', 'money')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('userBets', sa.Column('money', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('bet_slip', sa.Column('odds2', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('bet_slip', sa.Column('team1', sa.VARCHAR(length=300), autoincrement=False, nullable=True))
    op.add_column('bet_slip', sa.Column('team2', sa.VARCHAR(length=300), autoincrement=False, nullable=True))
    op.drop_column('bet_slip', 'teamWon')
    # ### end Alembic commands ###