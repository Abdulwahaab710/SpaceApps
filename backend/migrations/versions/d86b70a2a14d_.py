"""empty message

Revision ID: d86b70a2a14d
Revises: 
Create Date: 2017-04-30 00:39:04.186431

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd86b70a2a14d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bird',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('bird_name', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('spotted_bird',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('gps_lat', sa.Float(), nullable=True),
    sa.Column('gps_long', sa.Float(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('bird_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['bird_id'], ['bird.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('post')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('title', mysql.VARCHAR(length=128), nullable=True),
    sa.Column('body', mysql.TEXT(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.drop_table('spotted_bird')
    op.drop_table('bird')
    # ### end Alembic commands ###
