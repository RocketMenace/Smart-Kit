from typing import Self

from app.schemas.history import RequestInputSchema, RequestOutputSchema
from app.services.base import BaseServiceProtocol
from app.services.request import RequestServiceProtocol


class SaveResponseUseCase:
    def __init__(
        self: Self,
        history_service: BaseServiceProtocol,
        request_service: RequestServiceProtocol,
    ):
        self.history_service = history_service
        self.request_service = request_service

    async def get_response(self: Self, request: RequestInputSchema):
        response = await self.request_service.send_data(request=request)
        dto = RequestOutputSchema(
            cadastral_number=request.cadastral_number,
            latitude=request.latitude,
            longitude=request.longitude,
            response=response,
        )
        return await self.history_service.create(schema=dto)
