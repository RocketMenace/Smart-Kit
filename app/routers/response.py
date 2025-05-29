from fastapi import APIRouter, status, Depends
from app.schemas.history import RequestInputSchema
from app.dependencies.use_cases import get_process_request_use_case
from app.use_cases.process_request import ProcessRequestUseCase
from typing import Annotated
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/third-party-server", tags=["Response server"])


@router.post("/result", status_code=status.HTTP_200_OK, response_class=JSONResponse)
async def get_response(request: RequestInputSchema, use_case: Annotated[ProcessRequestUseCase, Depends(get_process_request_use_case)]):
    return await use_case.third_party_service.process_request()


@router.get("/ping", status_code=status.HTTP_200_OK)
async def ping_server():
    pass
