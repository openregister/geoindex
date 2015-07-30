"""empty message

Revision ID: a69e40268f
Revises: None
Create Date: 2015-07-30 15:20:50.955082

"""

# revision identifiers, used by Alembic.
revision = 'a69e40268f'
down_revision = None

from alembic import op
import sqlalchemy as sa
import geoalchemy2


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('boundary',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('polygon', geoalchemy2.types.Geometry(geometry_type='MULTIPOLYGON', srid=4326), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('boundary')
    ### end Alembic commands ###