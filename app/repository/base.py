from typing import TypeVar, Self, Protocol

from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from app.config.database import database

DBModel = TypeVar("DBModel", bound=database.Base)
T = TypeVar("T")


class BaseRepositoryProtocol(Protocol):
    async def add_one(self: Self, entity: T) -> T: ...

    async def get_all(self: Self) -> list[T]: ...


class BaseRepository(BaseRepositoryProtocol):
    def __init__(self, session: AsyncSession, model: DBModel):
        self.session = session
        self.model = model

    async def add_one(self: Self, entity: T) -> T:
        async with self.session as session:
            try:
                session.add(entity)
                await session.commit()
                await session.refresh()
                return entity
            except IntegrityError as error:
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT, detail=str(error)
                )

    async def get_all(self: Self) -> list[T]:
        async with self.session as session:
            stmt = select(self.model)
            result = await session.execute(stmt)
            return result.scalars().all()
