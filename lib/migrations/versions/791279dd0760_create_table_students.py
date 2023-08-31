"""create table students

Revision ID: 791279dd0760
Revises: 6b9cb35ba46e
Create Date: 2022-12-20 10:05:32.829662

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '791279dd0760'
down_revision = '6b9cb35ba46e'
branch_labels = None
depends_on = None


def upgrade() -> None:
     op.rename_table('scholars', 'students')



def downgrade() -> None:
    op.rename_table('students', 'scholars')

