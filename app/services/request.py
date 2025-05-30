from typing import Protocol, Self
from httpx import AsyncClient

from app.schemas.history import RequestInputSchema


class RequestServiceProtocol(Protocol):
    async def send_data(self: Self, request: RequestInputSchema) -> bool: ...


class RequestService(RequestServiceProtocol):
    def __init__(self: Self, http_client: AsyncClient):
        self.http_client = http_client

    async def send_data(self: Self, request: RequestInputSchema) -> bool:
        async with self.http_client as client:
            return await self.http_client.post()
