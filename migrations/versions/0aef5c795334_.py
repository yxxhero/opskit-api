"""empty message

Revision ID: 0aef5c795334
Revises: 962416b0fbae
Create Date: 2019-02-28 21:08:05.587471

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0aef5c795334'
down_revision = '962416b0fbae'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('note', sa.Column('is_public', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('note', 'is_public')
    # ### end Alembic commands ###
