from app.services.base import BaseService
from app.repository.base import BaseRepositoryProtocol
from typing import Self
from app.schemas.user import UserCreateSchema


class UserService(BaseService):
    def __init__(self, repository: BaseRepositoryProtocol):
        self.repository = repository
        super().__init__(repository=repository)

    async def create(self: Self, schema: UserCreateSchema):
        return await self.repository.add_one(schema=schema)
