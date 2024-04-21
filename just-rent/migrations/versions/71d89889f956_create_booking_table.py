"""Create booking table

Revision ID: 71d89889f956
Revises: 4822a0b50de6
Create Date: 2024-04-22 00:24:50.213196

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '71d89889f956'
down_revision = '4822a0b50de6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('booking',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('car_id', sa.Integer(), nullable=True),
    sa.Column('rent_location_id', sa.Integer(), nullable=True),
    sa.Column('return_location_id', sa.Integer(), nullable=True),
    sa.Column('pickup_date', sa.DateTime(), nullable=True),
    sa.Column('return_date', sa.DateTime(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('status', sa.String(length=255), nullable=False),
    sa.ForeignKeyConstraint(['car_id'], ['cars.id'], ),
    sa.ForeignKeyConstraint(['rent_location_id'], ['location.id'], ),
    sa.ForeignKeyConstraint(['return_location_id'], ['location.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('booking', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_booking_pickup_date'), ['pickup_date'], unique=False)
        batch_op.create_index(batch_op.f('ix_booking_return_date'), ['return_date'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('booking', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_booking_return_date'))
        batch_op.drop_index(batch_op.f('ix_booking_pickup_date'))

    op.drop_table('booking')
    # ### end Alembic commands ###
