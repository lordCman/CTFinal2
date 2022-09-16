"""empty message

Revision ID: be94011d9584
Revises: dbf2b1fcaf7a
Create Date: 2022-08-30 08:42:16.387804

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'be94011d9584'
down_revision = 'dbf2b1fcaf7a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('userBets',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('bet_slip_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['bet_slip_id'], ['bet_slip.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('userBets')
    # ### end Alembic commands ###