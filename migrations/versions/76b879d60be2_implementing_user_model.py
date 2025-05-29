"""Implementing user model.

Revision ID: 76b879d60be2
Revises: 4c3c452db0a0
Create Date: 2025-05-29 04:09:35.501481

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "76b879d60be2"
down_revision: Union[str, None] = "4c3c452db0a0"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    conn = op.get_bind()
    conn.execute(
        sa.text(
            "CREATE TABLE IF NOT EXISTS users"
            "(id UUID PRIMARY KEY,"
            "email VARCHAR(50) NOT NULL,"
            "first_name VARCHAR(50) NOT NULL,"
            "last_name VARCHAR(50) NOT NULL,"
            "created_at TIMESTAMPTZ DEFAULT NOW(),"
            "password VARCHAR(128) NOT NULL)"
        )
    )


def downgrade() -> None:
    """Downgrade schema."""

    conn = op.get_bind()
    conn.execute(sa.text("DROP TABLE IF EXISTS users"))
