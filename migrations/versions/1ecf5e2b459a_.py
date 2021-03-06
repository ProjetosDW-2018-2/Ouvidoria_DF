"""empty message

Revision ID: 1ecf5e2b459a
Revises: dc4f394ead69
Create Date: 2019-01-09 11:36:09.182572

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1ecf5e2b459a'
down_revision = 'dc4f394ead69'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('endereco',
    sa.Column('id_endereco', sa.Integer(), nullable=False),
    sa.Column('latitude', sa.String(length=30), nullable=True),
    sa.Column('longitude', sa.String(length=30), nullable=True),
    sa.Column('des_endereco', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id_endereco')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('endereco')
    # ### end Alembic commands ###
