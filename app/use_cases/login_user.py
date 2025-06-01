from app.services.auth import AuthService
from typing import Self, Any
from app.auth.schemas import UserLoginSchema


class LoginUserUseCase:
    def __init__(self: Self, auth_service: AuthService):
        self.auth_service = auth_service

    async def login_user(self: Self, schema: UserLoginSchema) -> dict[str, Any]:
        return await self.auth_service.login(schema=schema)

    async def logout_user(self: Self):
        return await self.auth_service.logout()

    async def refresh_token(self: Self, token: str) -> dict[str, str]:
        return await self.auth_service.refresh(token=token)
