"""empty message

Revision ID: a440dc2f16a8
Revises: b0f1360bbb21
Create Date: 2019-02-01 15:46:28.443331

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a440dc2f16a8'
down_revision = 'b0f1360bbb21'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('user_avatar', sa.String(length=512), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'user_avatar')
    # ### end Alembic commands ###