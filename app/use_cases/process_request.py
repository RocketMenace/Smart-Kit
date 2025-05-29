from typing import Self

class ProcessRequestUseCase:

    def __init__(self: Self, third_party_service):
        self.third_party_service = third_party_service

    def process_request(self: Self, schema):
        pass