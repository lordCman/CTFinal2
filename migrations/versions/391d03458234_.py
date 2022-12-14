"""empty message

Revision ID: 391d03458234
Revises: be94011d9584
Create Date: 2022-09-02 16:38:05.009219

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '391d03458234'
down_revision = 'be94011d9584'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('userBets', sa.Column('active', sa.Boolean(), nullable=True))
    op.add_column('userBets', sa.Column('won', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('userBets', 'won')
    op.drop_column('userBets', 'active')
    # ### end Alembic commands ###
