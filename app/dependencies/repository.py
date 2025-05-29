from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.config.database import database
from app.repository.base import BaseRepositoryProtocol
from app.repository.history import HistoryRepository
from app.repository.user import UserRepository


async def get_user_repository(
        session: Annotated[AsyncSession, Depends(database.get_session)]
) -> BaseRepositoryProtocol:
    return UserRepository(session=session)

async def get_history_repository(
    session: Annotated[AsyncSession, Depends(database.get_session)]
) -> BaseRepositoryProtocol:
    return HistoryRepository(session=session)
