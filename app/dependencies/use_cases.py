from typing import Annotated

from fastapi import Depends

from app.dependencies.services import get_history_service, get_request_service
from app.services.history import HistoryService
from app.services.request import RequestService
from app.use_cases.get_response import SaveResponseUseCase
from app.use_cases.register_user import UserRegisterUseCase
from app.services.user import UserService
from app.dependencies.services import get_user_service
from app.dependencies.services import get_third_party_service
from app.services.third_party import ThirdPartyService
from app.use_cases.process_request import ProcessRequestUseCase


async def get_user_register_use_case(
    user_service: Annotated[UserService, Depends(get_user_service)],
) -> UserRegisterUseCase:
    return UserRegisterUseCase(user_service=user_service)


async def get_save_response_use_case(
    history_service: Annotated[HistoryService, Depends(get_history_service)],
    request_service: Annotated[RequestService, Depends(get_request_service)],
) -> SaveResponseUseCase:
    return SaveResponseUseCase(
        history_service=history_service, request_service=request_service
    )


async def get_process_request_use_case(
    third_party_service: Annotated[ThirdPartyService, Depends(get_third_party_service)],
) -> ProcessRequestUseCase:
    return ProcessRequestUseCase(third_party_service=third_party_service)
