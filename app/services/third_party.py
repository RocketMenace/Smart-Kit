from typing import Self
from random import randint


class ThirdPartyService:
    def __init__(self: Self):
        pass

    def process_request(self: Self):
        response_body = bool(randint(0,1))
        return {"response": response_body}
