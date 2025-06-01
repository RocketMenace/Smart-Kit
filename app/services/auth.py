from typing import Self
from app.repository.user import UserRepository
from app.auth.schemas import UserLoginSchema


class AuthService:

    def __init__(self: Self, repository: UserRepository):
        self.repository = repository

    async def login(self: Self, schema: UserLoginSchema):
        user = self.repository