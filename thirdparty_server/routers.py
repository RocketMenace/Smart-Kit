from fastapi import APIRouter, status, Depends

from thirdparty_server.schemas import RequestInputSchema

from typing import Annotated
from fastapi.responses import JSONResponse
from thirdparty_server.dependencies import get_process_request_use_case
from thirdparty_server.use_cases import ProcessRequestUseCase

router = APIRouter(tags=["Response server"])


@router.post("/result", status_code=status.HTTP_200_OK, response_class=JSONResponse)
async def get_response(
    request: RequestInputSchema,
    use_case: Annotated[ProcessRequestUseCase, Depends(get_process_request_use_case)],
):
    return await use_case.process_request(schema=request)


@router.get("/ping", status_code=status.HTTP_200_OK, response_class=JSONResponse)
async def ping_server(
    use_case: Annotated[ProcessRequestUseCase, Depends(get_process_request_use_case)],
):
    return await use_case.ping()
