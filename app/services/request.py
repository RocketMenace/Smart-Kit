from typing import Self, Protocol
from app.schemas.history import RequestSchema


class RequestServiceProtocol(Protocol):
    async def get_response(self: Self, request: RequestSchema) -> bool: ...


class RequestService(RequestServiceProtocol):
    async def get_response(self: Self, request: RequestSchema) -> bool:
        pass
