from typing import Any, Protocol, Self
from pydantic import BaseModel
from app.repository.base import BaseRepositoryProtocol


class BaseServiceProtocol(Protocol):
    async def create(self: Self, schema: Any): ...

    async def get_all(self: Self): ...


class BaseService(BaseServiceProtocol):
    def __init__(self: Self, repository: BaseRepositoryProtocol):
        self.repository = repository

    async def create(self: Self, schema: BaseModel) -> Any: 
        return await self.repository.add_one(schema=schema)

    async def get_all(self: Self):
        return await self.repository.get_all()
