from fastapi import APIRouter, status, Depends
from app.schemas.history import HistoryResponseSchema
from typing import Annotated

from app.dependencies.use_cases import get_history_use_case
from app.use_cases.get_history import GetHistoryUseCase
from app.auth.dependencies import get_current_user

router = APIRouter(
    prefix="/history", dependencies=[Depends(get_current_user)], tags=["Service"]
)


@router.get(
    "",
    status_code=status.HTTP_200_OK,
    response_model=list[HistoryResponseSchema],
    description="Retrieve request history",
    responses={
        status.HTTP_200_OK: {
            "model": list[HistoryResponseSchema],
            "description": "Successful response",
        },
        status.HTTP_401_UNAUTHORIZED: {"description": "Unauthorized"},
    },
)
async def get_history(
    use_case: Annotated[GetHistoryUseCase, Depends(get_history_use_case)],
):
    return await use_case.get_history()
