from typing import Protocol, Self, Sequence, TypeVar

from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel

from app.config.database import database

DBModel = TypeVar("DBModel", bound=database.Base)


class BaseRepositoryProtocol(Protocol):
    async def add_one(self: Self, schema: BaseModel) -> DBModel: ...

    async def get_all(self: Self) -> Sequence[DBModel]: ...


class BaseRepository(BaseRepositoryProtocol):
    def __init__(self, session: AsyncSession, model: DBModel):
        self.session = session
        self.model = model

    async def add_one(self: Self, schema: BaseModel) -> DBModel:
        async with self.session as session:
            try:
                entity = self.model(**schema.model_dump())
                session.add(entity)
                await session.commit()
                await session.refresh(entity)
                return entity
            except IntegrityError as error:
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT, detail=str(error)
                )

    async def get_all(self: Self) -> Sequence[DBModel]:
        async with self.session as session:
            stmt = select(self.model)
            result = await session.execute(stmt)
            return result.scalars().all()
