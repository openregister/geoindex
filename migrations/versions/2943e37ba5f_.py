"""empty message

Revision ID: 2943e37ba5f
Revises: a69e40268f
Create Date: 2015-07-31 14:24:08.162295

"""

# revision identifiers, used by Alembic.
revision = '2943e37ba5f'
down_revision = 'a69e40268f'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('boundary', sa.Column('code', sa.String(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('boundary', 'code')
    ### end Alembic commands ###
