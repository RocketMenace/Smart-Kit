from app.services.request import RequestServiceProtocol
from typing import Self


class CheckServerUseCase:
    def __init__(self, request_service: RequestServiceProtocol):
        self.request_service = request_service

    async def ping_server(self: Self):
        return await self.request_service.ping_third_party_server()
