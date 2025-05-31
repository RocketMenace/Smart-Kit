from typing import Protocol, Self, Any
from app.infrastructure.http_client import AsyncHTTPClient

from app.schemas.history import RequestInputSchema
from fastapi.responses import Response


class RequestServiceProtocol(Protocol):
    async def send_data(self: Self, schema: RequestInputSchema) -> dict[str, Any]: ...

    async def ping_third_party_server(self: Self) -> Response: ...


class RequestService(RequestServiceProtocol):
    def __init__(self: Self, http_client: AsyncHTTPClient):
        self.http_client = http_client

    async def send_data(self: Self, schema: RequestInputSchema) -> dict[str, Any]:
        response = await self.http_client.post(
            endpoint="http://localhost:8080/api/third-party-server/result", json=schema.model_dump()
        )
        return response.json()

    async def ping_third_party_server(self: Self) -> Response:
        response = await self.http_client.get(endpoint="http://localhost:8080/api/third-party-server/ping")
        return response
