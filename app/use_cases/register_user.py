from typing import Self
from app.services.base import BaseServiceProtocol
from app.schemas.user import UserCreateSchema


class UserRegisterUseCase:

    def __init__(self: Self, service: BaseServiceProtocol):

        self.service = service

    async def register(self: Self, schema: UserCreateSchema):
        return await self.service.create(schema=schema)


