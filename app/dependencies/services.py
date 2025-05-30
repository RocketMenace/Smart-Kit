from typing import Annotated

from fastapi import Depends

from app.dependencies.repository import get_history_repository, get_user_repository
from app.infrastructure.http_client import AsyncHTTPClient
from app.repository.history import HistoryRepository
from app.services.base import BaseServiceProtocol
from app.services.history import HistoryService
from app.services.request import RequestService, RequestServiceProtocol
from app.repository.user import UserRepository
from app.services.user import UserService
from app.services.third_party import ThirdPartyService


async def get_http_client() -> AsyncHTTPClient:
    return AsyncHTTPClient(base_url="http://localhost:8000")


async def get_user_service(
    repository: Annotated[UserRepository, Depends(get_user_repository)],
) -> BaseServiceProtocol:
    return UserService(repository=repository)


async def get_history_service(
    repository: Annotated[HistoryRepository, Depends(get_history_repository)],
) -> BaseServiceProtocol:
    return HistoryService(repository=repository)


async def get_request_service(
    http_clienT: Annotated[AsyncHTTPClient, Depends(get_http_client)],
) -> RequestServiceProtocol:
    return RequestService(http_client=http_clienT)


async def get_third_party_service():
    return ThirdPartyService()
