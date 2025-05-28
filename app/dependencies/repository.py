from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.config.database import database
from app.models.history import RequestHistory
from app.repository.base import BaseRepositoryProtocol
from app.repository.history import HistoryRepository


async def get_history_repository(
    session: Annotated[AsyncSession, Depends(database.get_session)],
    model: RequestHistory,
) -> BaseRepositoryProtocol:
    return HistoryRepository(session=session, model=model)
