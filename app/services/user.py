from app.services.base import BaseService
from app.repository.base import BaseRepositoryProtocol
from typing import Self
from app.schemas.user import UserCreateSchema
from app.auth.security import hash_password
from app.models.user import User


class UserService(BaseService):
    def __init__(self, repository: BaseRepositoryProtocol):
        self.repository = repository
        super().__init__(repository=repository)

    async def create(self: Self, schema: UserCreateSchema) -> User:
        schema.password = hash_password(schema.password)
        return await self.repository.add_one(schema=schema)
