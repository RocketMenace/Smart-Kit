from typing import Annotated

from fastapi import Depends

from app.services.history import HistoryService
from app.services.request import RequestService
from app.use_cases.get_response import SaveResponseUseCase
from app.use_cases.register_user import UserRegisterUseCase
from app.services.user import UserService
from app.dependencies.services import (
    get_user_service,
    get_auth_service,
    get_history_service,
    get_request_service,
)
from app.use_cases.get_history import GetHistoryUseCase
from app.use_cases.check_server import CheckServerUseCase
from app.services.auth import AuthService
from app.use_cases.login_user import LoginUserUseCase


async def get_user_login_use_case(
    auth_service: Annotated[AuthService, Depends(get_auth_service)],
) -> LoginUserUseCase:
    return LoginUserUseCase(auth_service=auth_service)


async def get_user_register_use_case(
    user_service: Annotated[UserService, Depends(get_user_service)],
) -> UserRegisterUseCase:
    return UserRegisterUseCase(user_service=user_service)


async def get_check_server_use_case(
    request_service: Annotated[RequestService, Depends(get_request_service)],
) -> CheckServerUseCase:
    return CheckServerUseCase(request_service=request_service)


async def get_save_response_use_case(
    history_service: Annotated[HistoryService, Depends(get_history_service)],
    request_service: Annotated[RequestService, Depends(get_request_service)],
) -> SaveResponseUseCase:
    return SaveResponseUseCase(
        history_service=history_service, request_service=request_service
    )


async def get_history_use_case(
    history_service: Annotated[HistoryService, Depends(get_history_service)],
) -> GetHistoryUseCase:
    return GetHistoryUseCase(history_service=history_service)
