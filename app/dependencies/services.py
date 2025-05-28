from typing import Annotated

from fastapi import Depends

from app.dependencies.repository import get_history_repository
from app.repository.history import HistoryRepository
from app.services.base import BaseServiceProtocol
from app.services.history import HistoryService
from app.services.request import RequestService, RequestServiceProtocol


async def get_history_service(
    repository: Annotated[HistoryRepository, Depends(get_history_repository)],
) -> BaseServiceProtocol:
    return HistoryService(repository=repository)


async def get_request_service() -> RequestServiceProtocol:
    return RequestService
