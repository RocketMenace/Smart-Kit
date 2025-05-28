from typing import Annotated

from fastapi import APIRouter, Depends, status

from app.dependencies.use_cases import get_save_response_use_case
from app.schemas.history import HistoryResponseSchema, RequestInputSchema
from app.use_cases.get_response import SaveResponseUseCase

router = APIRouter()


@router.post(
    path="/query",
    response_model=HistoryResponseSchema,
    status_code=status.HTTP_201_CREATED,
)
async def register_cadastral_record(
    request: RequestInputSchema,
    use_case: Annotated[SaveResponseUseCase, Depends(get_save_response_use_case)],
):
    return await use_case.get_response(request=request)
