from typing import Protocol, Self

from app.schemas.history import RequestInputSchema


class RequestServiceProtocol(Protocol):
    async def get_response(self: Self, request: RequestInputSchema) -> bool: ...


class RequestService(RequestServiceProtocol):
    async def get_response(self: Self, request: RequestInputSchema) -> bool:
        pass
