from typing import Self
from app.services.base import BaseServiceProtocol
from app.schemas.user import UserCreateSchema


class UserRegisterUseCase:
    def __init__(self: Self, user_service: BaseServiceProtocol):
        self.user_service = user_service

    async def register(self: Self, schema: UserCreateSchema):
        return await self.user_service.create(schema=schema)
