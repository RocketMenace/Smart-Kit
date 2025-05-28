from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.history import RequestHistory
from app.repository.base import BaseRepository


class HistoryRepository(BaseRepository):
    def __init__(self, session: AsyncSession, model: RequestHistory):
        self.session = session
        super().__init__(session, model)

    async def get_by_cadastral_number(self, cadastral_number: str) -> RequestHistory:
        async with self.session as session:
            stmt = select(self.model).where(
                self.model.cadastral_number == cadastral_number
            )
            result = await session.execute(stmt)
            return result.scalar_one_or_none()
