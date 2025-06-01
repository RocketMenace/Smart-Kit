from typing import Self
from uuid import UUID

from app.repository.base import BaseRepository
from app.models.user import User
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select


class UserRepository(BaseRepository):
    def __init__(self, session: AsyncSession):
        self.session = session
        super().__init__(session, model=User)

    async def get_by_uuid(self: Self, uuid: UUID) -> User:
        async with self.session as session:
            stmt = select(User).where(User.id == uuid)
            result = await session.execute(stmt)
            return result.scalar_one_or_none()

    async def get_by_email(self: Self, email: str) -> User:
        async with self.session as session:
            stmt = select(User).where(User.email == email)
            result = await session.execute(stmt)
            return result.scalar_one_or_none()