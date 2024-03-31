"""empty message

Revision ID: 9063a8b1b30f
Revises: 65fe88f672c3
Create Date: 2024-03-31 20:43:50.282141

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9063a8b1b30f'
down_revision = '65fe88f672c3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('author', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_author_lastname'), ['lastname'], unique=False)
        batch_op.create_index(batch_op.f('ix_author_name'), ['name'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('author', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_author_name'))
        batch_op.drop_index(batch_op.f('ix_author_lastname'))

    # ### end Alembic commands ###
