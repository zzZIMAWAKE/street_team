"""Set up sale, user, item and reward table

Revision ID: 34632f7713e5
Revises: 
Create Date: 2017-06-24 10:00:20.373280

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '34632f7713e5'
down_revision = None
branch_labels = None
depends_on = None


# Future improvements would include a campaign table so that that this can be set up for several different
# campaigns at a time
def upgrade():
    conn = op.get_bind()

    op.create_table(
        'user',
        sa.Column('id', sa.BigInteger(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table(
        'item',
        sa.Column('id', sa.BigInteger(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table(
        'reward',
        sa.Column('id', sa.BigInteger(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('category', sa.Integer(), nullable=False),
        sa.Column('points', sa.Integer(), nullable=False),
        sa.Column('max_per_user', sa.Integer(), nullable=False),
        sa.Column('global_max', sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table(
        'sale',
        sa.Column('id', sa.BigInteger(), nullable=False),
        sa.Column('item_id', sa.BigInteger(), nullable=False),
        sa.Column('cost', sa.Float(), nullable=False),
        sa.Column('currency', sa.String(), server_default='GBP', nullable=False),
        sa.Column('user_id', sa.BigInteger()),
        sa.PrimaryKeyConstraint('id'),
        sa.ForeignKeyConstraint(['user_id'], ['user.id']),
        sa.ForeignKeyConstraint(['item_id'], ['item.id'])
    )
    rewards = [
        {"name": "General Ticket", "category": '1', "points": '100', "max_per_user": '5', "global_max": '1000'},
        {"name": "VIP Ticket", "category": '1', "points": '1000', "max_per_user": '1', "global_max": '50'},
        {"name": "Weekend Ticket", "category": '2', "points": '250', "max_per_user": '2', "global_max": '500'},
        {"name": "Free Drink Voucher", "category": '3', "points": '50', "max_per_user": '10'},
        {"name": "Free Limo to event", "category": '4', "points": '5000', "max_per_user": '1', "global_max": '1'}
    ]

    user_ids = [12345, 76543, 234567, 987654, 23456, 87654]

    for reward in rewards:
        keys = [key for key in reward.keys()]
        values = [value for value in reward.values()]

        statement = "INSERT INTO reward ("
        statement += ", ".join(keys)
        statement += ") VALUES ('"
        statement += "', '".join(values)
        statement += "')"

        conn.execute(statement)

    for user_id in user_ids:
        conn.execute('INSERT INTO "user" (id) VALUES ({})'.format(user_id))

    for item_id in range(1, 20):
        conn.execute('INSERT INTO item (id) VALUES ({})'.format(item_id))


def downgrade():
    op.drop_table('sale')
    op.drop_table('reward')
    op.drop_table('item')
    op.drop_table('user')
