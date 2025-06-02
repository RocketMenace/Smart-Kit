from fastapi import HTTPException, status
from jwt import InvalidTokenError

from app.infrastructure.redis import RedisClient
from app.services.auth import AuthService
from typing import Self, Any
from app.auth.schemas import UserLoginSchema
from app.auth.jwt import decode_jwt
from datetime import datetime, timezone


class LoginUserUseCase:
    def __init__(self: Self, auth_service: AuthService, cache: RedisClient):
        self.auth_service = auth_service
        self.cache = cache

    async def login_user(self: Self, schema: UserLoginSchema) -> dict[str, Any]:
        return await self.auth_service.login(schema=schema)

    async def logout_user(self: Self, token: str):
        try:
            payload = decode_jwt(token)
            ttl = datetime.fromtimestamp(payload.get("exp")) - datetime.now(
                tz=timezone.utc
            )
            await self.cache.set(key=token, value="Blacklisted", ttl=ttl)
            return await self.auth_service.logout()
        except InvalidTokenError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid token."
            )

    async def refresh_token(self: Self, token: str) -> dict[str, str]:
        if await self.cache.get(key=token):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid token."
            )
        return await self.auth_service.refresh(token=token)
