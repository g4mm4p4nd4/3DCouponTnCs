"""create articles

Revision ID: cd621026971e
Revises: 
Create Date: 2025-06-15 08:41:36.769499

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cd621026971e'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'articles',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('title', sa.String, nullable=False),
        sa.Column('url', sa.String, nullable=False, unique=True),
        sa.Column('source', sa.String),
        sa.Column('published_at', sa.DateTime),
        sa.Column('content', sa.Text),
        sa.Column('score', sa.Float),
        sa.Column('dedup_hash', sa.String),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('articles')
