"""empty message

Revision ID: dbf2b1fcaf7a
Revises: 
Create Date: 2022-08-30 08:39:33.350507

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dbf2b1fcaf7a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bet_slip',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('team1', sa.String(length=300), nullable=True),
    sa.Column('team2', sa.String(length=300), nullable=True),
    sa.Column('odds1', sa.Integer(), nullable=True),
    sa.Column('odds2', sa.Integer(), nullable=True),
    sa.Column('oddsTie', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=150), nullable=False),
    sa.Column('password', sa.String(length=250), nullable=False),
    sa.Column('apitoken', sa.String(), nullable=True),
    sa.Column('level', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('caption', sa.String(length=300), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post')
    op.drop_table('user')
    op.drop_table('bet_slip')
    # ### end Alembic commands ###
