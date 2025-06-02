from typing import Annotated

from fastapi import APIRouter, Depends, status

from app.dependencies.use_cases import get_save_response_use_case
from app.schemas.history import HistoryResponseSchema, RequestInputSchema
from app.use_cases.get_response import SaveResponseUseCase
from app.use_cases.check_server import CheckServerUseCase
from app.dependencies.use_cases import get_check_server_use_case
from app.auth.dependencies import get_current_user

router = APIRouter(dependencies=[Depends(get_current_user)], tags=["Service"])


@router.post(
    path="/query",
    response_model=HistoryResponseSchema,
    status_code=status.HTTP_201_CREATED,
    description="Register cadastral record.",
    responses={
        status.HTTP_201_CREATED: {
            "model": HistoryResponseSchema,
            "description": "Successful response",
        },
        status.HTTP_401_UNAUTHORIZED: {"description": "Unauthorized"},
    },
)
async def register_cadastral_record(
    request: RequestInputSchema,
    use_case: Annotated[SaveResponseUseCase, Depends(get_save_response_use_case)],
):
    return await use_case.get_response(request=request)


@router.get(
    path="/ping",
    status_code=status.HTTP_200_OK,
    description="Checking condition of third party server.",
    responses={status.HTTP_401_UNAUTHORIZED: {"description": "Unauthorized"}},
)
async def health_check_server(
    use_case: Annotated[CheckServerUseCase, Depends(get_check_server_use_case)],
):
    return await use_case.ping_server()
