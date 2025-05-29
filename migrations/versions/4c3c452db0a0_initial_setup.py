"""Initial setup.

Revision ID: 4c3c452db0a0
Revises:
Create Date: 2025-05-29 02:41:38.731807

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "4c3c452db0a0"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    conn = op.get_bind()
    conn.execute(
        sa.text(
            "CREATE TABLE IF NOT EXISTS request_history "
            "(id SERIAL PRIMARY KEY,"
            "cadastral_number VARCHAR(255) NOT NULL UNIQUE,"
            "latitude DECIMAL(4) NOT NULL,"
            "longitude DECIMAL(4) NOT NULL,"
            "response BOOLEAN NOT NULL,"
            "created_at TIMESTAMPTZ DEFAULT NOW());"
        )
    )


def downgrade() -> None:
    """Downgrade schema."""

    conn = op.get_bind()
    conn.execute(sa.text("DROP TABLE IF EXISTS request_history"))
