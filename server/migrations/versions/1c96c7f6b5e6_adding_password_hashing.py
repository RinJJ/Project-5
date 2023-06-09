"""adding password hashing

Revision ID: 1c96c7f6b5e6
Revises: b3d1c3797192
Create Date: 2023-05-03 08:29:30.547589

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1c96c7f6b5e6'
down_revision = 'b3d1c3797192'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('_password_hash', sa.String(), nullable=True))
        batch_op.drop_column('password')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password', sa.VARCHAR(length=50), nullable=False))
        batch_op.drop_column('_password_hash')

    # ### end Alembic commands ###
