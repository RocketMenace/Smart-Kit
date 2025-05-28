from pydantic import BaseModel, Field


class RequestBaseSchema(BaseModel):
    cadastral_number: str
    latitude: float
    longtitude: float


class RequestInputSchema(RequestBaseSchema):
    pass


class RequestOutputSchema(RequestBaseSchema):
    response: bool


class HistoryResponseSchema(RequestBaseSchema):
    id: int
    response: bool
