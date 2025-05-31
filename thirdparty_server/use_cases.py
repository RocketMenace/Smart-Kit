from typing import Self
from app.schemas.history import RequestInputSchema
from thirdparty_server.services import ThirdPartyService


class ProcessRequestUseCase:
    def __init__(self: Self, third_party_service: ThirdPartyService):
        self.third_party_service = third_party_service

    async def process_request(self: Self, schema: RequestInputSchema):
        return await self.third_party_service.process_request()

    async def ping(self: Self):
        return await self.third_party_service.ping()