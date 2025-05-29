from pydantic import BaseModel, Field, ConfigDict


class RequestBaseSchema(BaseModel):
    cadastral_number: str
    latitude: float
    longitude: float


class RequestInputSchema(RequestBaseSchema):
    pass


class RequestOutputSchema(RequestBaseSchema):
    response: bool


class HistoryResponseSchema(RequestBaseSchema):
    id: int
    response: bool
    model_config = ConfigDict(from_attributes=True)
