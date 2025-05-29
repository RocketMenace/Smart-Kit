from typing import Self
from app.services.third_party import ThirdPartyService


class ProcessRequestUseCase:
    def __init__(self: Self, third_party_service: ThirdPartyService):
        self.third_party_service = third_party_service

    def process_request(self: Self, schema):
        pass
