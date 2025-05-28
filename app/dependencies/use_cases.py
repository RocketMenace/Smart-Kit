from typing import Annotated

from fastapi import Depends

from app.dependencies.services import get_history_service, get_request_service
from app.services.history import HistoryService
from app.services.request import RequestService
from app.use_cases.get_response import SaveResponseUseCase


async def get_save_response_use_case(
    history_service: Annotated[HistoryService, Depends(get_history_service)],
    request_service: Annotated[RequestService, Depends(get_request_service)],
) -> SaveResponseUseCase:
    return SaveResponseUseCase(
        history_service=history_service, request_service=request_service
    )
