"""add address2

Revision ID: 683512dfdacf
Revises: 1acb16621eb8
Create Date: 2023-07-20 11:54:35.290499

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '683512dfdacf'
down_revision = '1acb16621eb8'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('address', sa.Column('address2', sa.String(), nullable=True))


def downgrade() -> None:
    pass
