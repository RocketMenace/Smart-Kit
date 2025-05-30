from typing import Self
from app.services.history import HistoryService


class GetHistoryUseCase:
    def __init__(self: Self, history_service: HistoryService):
        self.history_service = history_service

    async def get_history(self: Self):
        return await self.history_service.get_all()
