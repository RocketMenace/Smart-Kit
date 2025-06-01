from aioredis import Redis
from typing import Self, Any


class CacheService:
    def __init__(self, repository: Redis):
        self.repository = repository

    async def set_cache(self: Self, key: str, value: Any, expire) -> None:
        await self.repository.append(key=key, value=value)

    async def get_cache(self: Self, key: str) -> Any:
        return await self.repository.get(key)

    async def delete_cache(self: Self, key: str) -> None:
        await self.repository.delete(key)
