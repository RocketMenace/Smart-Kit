from typing import Self, Protocol, Any
from app.repository.base import BaseRepositoryProtocol


class BaseServiceProtocol(Protocol):

    async def create(self: Self):
        ...

    async def get_all(self: Self):
        ...

class BaseService(BaseServiceProtocol):

    def __init__(self: Self, repository: BaseRepositoryProtocol):
        self.repository = repository
        

    async def create(self: Self, schema: Any) -> Any:
        return self.repository.add_one(schema)

    async def get_all(self: Self, id: int):
        return self.repository.get_all()