from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column

from app.config.database import database
from uuid import uuid4, UUID
from sqlalchemy import UUID, String, text


class User(database.Base):

    __tablename__ = "users"
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4, nullable=False)
    email: Mapped[str]= mapped_column(String(50), nullable=False)
    first_name: Mapped[str] = mapped_column(String(50), nullable=False)
    last_name: Mapped[str] = mapped_column(String(50), nullable=False)
    created_at: Mapped[datetime] = mapped_column(server_default=text("TIMEZONE('utc', now())"))
    password: Mapped[str] = mapped_column(String(128), nullable=False)
                                                



