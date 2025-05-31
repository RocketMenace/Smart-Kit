from typing import Annotated

from fastapi import Depends

from thirdparty_server.services import ThirdPartyService
from thirdparty_server.use_cases import ProcessRequestUseCase


async def get_third_party_service():
    return ThirdPartyService()


async def get_process_request_use_case(
    third_party_service: Annotated[ThirdPartyService, Depends(get_third_party_service)],
) -> ProcessRequestUseCase:
    return ProcessRequestUseCase(third_party_service=third_party_service)
