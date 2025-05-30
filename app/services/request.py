from typing import Protocol, Self, Any
from app.infrastructure.http_client import AsyncHTTPClient

from app.schemas.history import RequestInputSchema


class RequestServiceProtocol(Protocol):
    async def send_data(self: Self, request: RequestInputSchema) -> dict[str, Any]: ...


class RequestService(RequestServiceProtocol):
    def __init__(self: Self, http_client: AsyncHTTPClient):
        self.http_client = http_client

    async def send_data(self: Self, schema: RequestInputSchema) -> dict[str, Any]:
        async with self.http_client as client:
            response = await self.http_client.post(
                endpoint="/result", json=schema.model_dump()
            )
            return response.json()
